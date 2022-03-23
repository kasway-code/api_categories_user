from flask_restful import reqparse, abort, Api, Resource
from utils.image1920 import photo
from utils.cleanArgs import clean_args
from utils.response2 import MessageResponse2
from controllers.ConnectionDB import ConnectionDB

from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import werkzeug

class put_category(Resource):
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type = int)
        parser.add_argument('name'     , type = str)
        parser.add_argument('image'    , type = werkzeug.datastructures.FileStorage, location='files')
        parser.add_argument('parent_id', type = int)
        parser.add_argument('is_health_category', type = str)
        parser.add_argument('is_market_category', type = str)
        args = parser.parse_args()
        models, db,uid,password = ConnectionDB()

        try: 
            if args['image']!= None:
                image = photo(args['image'])
            else:
                image = None
        except Exception as error: 
            category = models.execute_kw(
                db,uid,password,
                'product.category',
                'search_read',
                [[['id', '=',args['id']]]],
                {
                    'fields':['name', 'odoo_image_url', 'parent_id']
                }
            )
            response = MessageResponse2('Opps, hubo un error con la imagen.', category)
            return response, 400

        is_market_category = args['is_market_category'].upper() if args['is_market_category'] != None  else None
        is_health_category = args['is_health_category'].upper() if args['is_health_category'] != None  else None

        optionsBool = {
            'TRUE': True,
            'FALSE': False
        }
        try:
            is_health_category = optionsBool[is_health_category]
        except: 
            is_health_category = None
        
        try:
            is_market_category = optionsBool[is_market_category]    
        except: 
            is_market_category = None

        newValues = {
            'name':args['name'] , 
            'image_1920':image,
            'parent_id': args['parent_id'],
            'is_market_category': is_market_category,
            'is_health_category': is_health_category
        }
        newValues = clean_args(newValues)
        try:
            categoryEdited = models.execute_kw(
                db,uid,password,
                'product.category',
                'write',
                [[args['id']], newValues]
            )
            fields = [
                    'name', 
                    'odoo_image_url', 
                    'parent_id',
                    'is_market_category',
                    'is_health_category'
                ]
           
            category = models.execute_kw(
                db,uid,password,
                'product.category',
                'search_read',
                [[['id', '=',args['id']]]],
                {
                    'fields':fields
                }
            )
           
            response = MessageResponse2('Listo, datos cambiados.', category)
            return response, 200
        except:
            response = MessageResponse2('Ocurrió un error.', False)
            return response, 400
            
        