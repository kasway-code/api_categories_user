from flask_restful import Api
from flask import Flask, request
from flask_cors import CORS
from model.category import CategoryList
from model.get_categoryWithPagination        import get_categoryWithPagination
from model.CreateCategory                    import CreateCategory
from model.put_category                      import put_category
from model.get_categoriesParents             import get_categoriesParent
from model.SearcherCategory                  import SearcherCategory
from model.search_subcategory                import search_subcategory
from model.deleteCategory                    import deleteCateegory
from model.get_categoryWithProducts          import get_categoryWithProducts

app = Flask(__name__)
cors = CORS(app)
api = Api(app)
api.app.config['RESTFUL_JSON'] = {
    'ensure_ascii': False
}
api.app.config['JSON_AS_ASCII'] = False

version = '/v2/'
api.add_resource(CategoryList,                      '{}categories'.format(version))
api.add_resource(get_categoryWithPagination,        '{}categories/admin'.format(version))
api.add_resource(CreateCategory ,                   '{}category/create'.format(version))
api.add_resource(put_category ,                     '{}category/update'.format(version))
api.add_resource(get_categoriesParent,              '{}category/parent'.format(version))
api.add_resource(SearcherCategory,                  '{}category/search'.format(version))
api.add_resource(search_subcategory,            '{}subcategory/search'.format(version))
api.add_resource(deleteCateegory,                   '{}category/delete'.format(version))
api.add_resource(get_categoryWithProducts,          '{}categories/products'.format(version))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
