from flask_restful import reqparse, Api, Resource
from utils.pagination import page 
from utils.response import MessageResponse
from utils.get_dataAndTotal import get_dataAndTotal
from controllers.ConnectionDB import ConnectionDB


class get_categoryWithPagination(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('limit'  , type = int)
        parser.add_argument('offset'  , type = int)
        parser.add_argument('page'    , type = int)
        parser.add_argument('per_page'    , type = int)

        args = parser.parse_args()
        
        amountData = 10 if args['per_page'] == None else args['per_page']
        limit, offset = page(args['page'], args['limit'], args['offset'], amount= amountData)
        models,db,uid,password = ConnectionDB()
        category_list = [
            'name',
            'child_id',
            'parent_id',
            'odoo_image_url',
            'is_health_category',
            'is_market_category'
        ]
        domains = [
            '|',
            ['is_market_category', '=', True],
            ['is_health_category', '=', True]
        ]
        categories = models.execute_kw(
            db,uid,password, 'product.category',
            'search_read',
            [domains],
            {
                'fields': category_list
            }
        )
        for category in categories:
            if len(category['child_id']) != 0 :
                ids = category['child_id']
                childs = []
                for sub in categories:
                    if sub['id'] in ids:
                        a = {'id_child': sub['id'], 'name': sub['name'],  'odoo_image_url': sub['odoo_image_url']}
                        childs.append(a)
                category['child_id'] = childs

        indexs = []
        for index, category in enumerate(categories):
            if category['parent_id'] == False:
                indexs.append(index)

        selected_categories = []
        for index in indexs:
            selected_categories.append(categories[index])
        
        categories = []
        for category in selected_categories:
            del category['parent_id']
            if category['id'] != 1:
                categories.append(category)
        categories, total = get_dataAndTotal(categories, limit, offset)

        if total != 0:
            response = MessageResponse(
                'Categorías encontradas.',
                categories,
                args['page'],
                total
            )
            return response, 200

        else:
            response = MessageResponse(
                'Categorías no encontradas.',
                [],
                args['page'],
                total
            )
            return response, 200