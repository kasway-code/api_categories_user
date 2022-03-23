from flask_restful import Resource, reqparse
from controllers.ConnectionDB import ConnectionDB
from utils.pagination import page

from utils.response import MessageResponse
from utils.searcher import searcher

from utils.add_name_child import add_name_child

from field.field_search_subcategory import field_search_subcategory

class search_subcategory(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('value', type = str,required = True )
        parser.add_argument('limit', type = int)
        parser.add_argument('offset', type = int)
        parser.add_argument('page', type = int, required = True)
        parser.add_argument('per_page', type = int)
        args = parser.parse_args()
        

        models,db,uid,password = ConnectionDB()
        amountData = 10 if args['per_page'] == None else args['per_page']
        limit, offset = page(args['page'], args['limit'], args['offset'], amount= amountData)

        domains =  [
            ['name', 'ilike', args['value']],
            ['parent_id', '!=', None]
        ]
        fields = field_search_subcategory
        total = models.execute_kw(
            db,uid,password, 'product.category',
            'search_count',
            [domains]
        )
        data = models.execute_kw(
                db,uid,password, 'product.category',
                'search_read',
                [domains],
                {
                    'fields':fields,
                    'limit':limit,
                    'offset':offset
                }
        )
        message = 'Subcategoria encontrada' if total != 0 else 'Subcategoria no encontrada'
        response = MessageResponse(message, data, args['page'], total)
        return response, 200





