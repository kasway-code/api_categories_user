
from flask_restful import reqparse, abort, Api, Resource
from utils.image1920 import photo
from utils.cleanArgs import clean_args
from utils.response import MessageResponse
from utils.pagination import page
from controllers.ConnectionDB import ConnectionDB
import pandas as pd
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import werkzeug

class get_categoriesParent(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type = int)
        parser.add_argument('limit'     , type = str)
        parser.add_argument('offset'    ,type = int)
        parser.add_argument('per_page', type = int)
        args = parser.parse_args()
        models, db,uid,password = ConnectionDB()
        amountData = 10 if args['per_page'] == None else args['per_page']
        limit, offset = page(args['page'], args['limit'], args['offset'], amount= amountData)
        
        fields = [
            'name',
            'child_id',
            'parent_id',
            'odoo_image_url',
            'is_health_category',
            'is_market_category'
        ]

        domains = [
            ['parent_id', '=', False],
            '|',
            ['is_market_category', '=', True],
            ['is_health_category', '=', True]
        ]

        total = models.execute_kw(
            db, 
            uid, 
            password, 
            'product.category', 
            'search_count', 
            [domains])

        categoriesParent = models.execute_kw(
            db,uid,password, 'product.category',
            'search_read',
            [domains],
            {
                'fields':fields,
                'limit': limit,
                'offset': offset
            }
        )

        message = 'Categorías encontradas' if total!= 0 else 'Categorías no encontradas.'
        response = MessageResponse(message, categoriesParent, args['page'], total)

        return response, 200
