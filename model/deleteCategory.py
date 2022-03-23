from controllers.ConnectionDB import ConnectionDB
from flask_restful import Resource, reqparse
from utils.response2 import MessageResponse2
from utils.cleanArgs import clean_args

class deleteCateegory(Resource):
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('categoryID', type = int)
        args = parser.parse_args()
        models, db,uid,password = ConnectionDB()

        domains = [
            ['id', '=', args['categoryID']],
            ['is_market_category', '=', False],
            ['is_health_category', '=', False]
        ]
        categoryDeleted = models.execute_kw(
            db,uid,password,
            'product.category',
            'search_count',
            [domains]
        )

        if categoryDeleted == 1:
            return MessageResponse2('Lo sentimos, la categoría ya fue eliminada.', []), 400
        
        else:

            newValues = {
                'is_market_category': False,
                'is_health_category': False
            }
            newValues = clean_args(newValues)
            categoryDeleted = models.execute_kw(
                db,uid,password,
                'product.category',
                'write',
                [[args['categoryID']], newValues]
            )
            message = 'Categoría eliminada' if categoryDeleted == True else 'Opps, ocurrió un error al intentar eliminarlo'
            response = MessageResponse2(message, [])
            return response, 200       