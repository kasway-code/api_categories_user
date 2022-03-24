from flask_restful import reqparse, abort, Api, Resource

from common.get_categoryParent import get_categoryParent
from common.get_categories import get_categories
from model.CreateCategory import CreateCategory

class CategoryList(Resource):
    def __init__(self):
        self._model_name = "product.category"

    def get(self, store_id = None,user_id = None):

        parser = reqparse.RequestParser()
        parser.add_argument('parent_id'  , type = int)
        parser.add_argument('limit', type = int)
        parser.add_argument('offset', type = int)
        parser.add_argument('pag'     ,type=int)

        args = parser.parse_args()
        
        if type(args['parent_id']) == int:
            categoryParent = get_categoryParent(args)
            return categoryParent, 200

        else:
            categories = get_categories(args)
            return categories,200

