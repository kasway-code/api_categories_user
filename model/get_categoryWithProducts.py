from    flask_restful import reqparse, Api, Resource
from utils.pagination import page 
from utils.response2 import MessageResponse2
from utils.get_dataAndTotal import get_dataAndTotal
from controllers.ConnectionDB import ConnectionDB   
import pandas as pd
import json


class get_categoryWithProducts(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('limit'  , type = int)
        parser.add_argument('offset'  , type = int)
        parser.add_argument('page'    , type = int)
        parser.add_argument('per_page'    , type = int)
        parser.add_argument('warehouse_id'    , type = int)
        args = parser.parse_args()
        amountData = 10 if args['per_page'] == None else args['per_page']
        limit, offset = page(args['page'], args['limit'], args['offset'], amount= amountData)
        models,db,uid,password = ConnectionDB()
        category_list = [
            'name',
            'child_id',
            'parent_id',
            'warehouse_id',
            'categ_id',
            'odoo_image_url',
            'is_health_category',
            'is_market_category',
            'product_warehouse_count'
            #'product_warehouse_count' prueba, saber cuánto devuelve
            
            
            
        ]

        #Revisar product_warehouse_count
        domains = [
            '&',
            '|',
            ['is_market_category', '=', True],
            ['is_health_category', '=', True],
            '&',
            ['product_warehouse_count','>', 1],
            ['warehouse_id','=',args['warehouse_id']
            ]

        ]
        categories = models.execute_kw(
            db,uid,password, 'stock.warehouse.category',
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
                    
              
                    if sub['categ_id'][0] in ids and sub['product_warehouse_count']>0:
                        a = {'id_child': sub['categ_id'][0], 'name': sub['name'],  'odoo_image_url': sub['odoo_image_url'], 'count':sub['product_warehouse_count']}
                        childs.append(a)
                category['child_id'] = childs

        
        indexs = []
        for index, category in enumerate(categories):
            if category['parent_id'] == False and category['child_id']!=[]:
                indexs.append(index)

        selected_categories = []
        for index in indexs:
            selected_categories.append(categories[index])
        
        categories = []
        
        for category in selected_categories:
            del category['parent_id']
            if category['categ_id'] != 1:
                categories.append(category)
        categories, total = get_dataAndTotal(categories, limit, offset)
        

        '''
        categories = pd.DataFrame(categories)
        for col in categories.columns:
            print(col)
        categories.drop(columns=['product_warehouse_count','categ_id'])
        categories = categories.to_json(orient = 'records')
        categories = json.loads(categories)
        '''
        if total != 0:
            response = MessageResponse2(
                'Categorías encontradas.',
                categories,
            )
            return response, 200

        else:   
            response = MessageResponse2(
                'Categorías no encontradas.',
                [],

            )
            return response, 200