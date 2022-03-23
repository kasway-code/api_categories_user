import os
import json
from flask_restful import reqparse, Resource
from utils.image1920 import photo
from utils.cleanArgs import clean_args
from utils.response2 import MessageResponse2

import werkzeug
from controllers.ConnectionDB import ConnectionDB

class CreateCategory(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name'     , type = str)
        parser.add_argument('image'    , type = werkzeug.datastructures.FileStorage, location='files')
        parser.add_argument('parent_id', type = int)
        parser.add_argument('is_health_category', type = str)
        parser.add_argument('is_market_category', type = str)

        args = parser.parse_args()
        models,db,uid,password = ConnectionDB()
        
        try:
            image = photo(args['image'])
        except:
            image = None
            
        domains = [['name', '=',args['name']]]
        fields = ['id']
        is_market_category = args['is_market_category'].upper()
        is_health_category = args['is_health_category'].upper()

        optionsBool = {
            'TRUE': True,
            'FALSE': False
        }

        is_health_category = optionsBool[is_health_category]
        is_market_category = optionsBool[is_market_category]

        ask = models.execute_kw(
                db,uid,password, 'product.category',
                'search_count',
                [domains]
        )
        if ask == 0:
                newValues = {
                    'name':args['name'] , 
                    'image_1920':image,
                    'parent_id': args['parent_id'],
                    'is_market_category': is_market_category,
                    'is_health_category': is_health_category
                }
                newValues = clean_args(newValues)
                newCategory = models.execute_kw(
                    db,uid,password, 'product.category',
                    'create',
                    [newValues]
                )
                domains = [['id', '=', newCategory]]
                fields = [
                    'name', 
                    'odoo_image_url', 
                    'parent_id',
                    'is_market_category',
                    'is_health_category'
                ]

                data = models.execute_kw(
                    db,uid,password, 'product.category',
                    'search_read',
                    [domains],
                    {
                        'fields': fields
                    }
                )
                if args['parent_id'] == None:
                    response = MessageResponse2('Listo, categoría creada.', data)
                else:   
                    response = MessageResponse2('Listo, subcategoría creada.', data)
                return response, 200
        else:
                response = MessageResponse2('Error, esta categoría ya esta creada.', [])
                return response, 400
        