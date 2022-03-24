
from controllers.ConnectionDB import ConnectionDB

def get_categoryParent(args):

    models, db,uid,password = ConnectionDB()
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
        db,uid,password,'product.category',
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
    
    category_parent = []
    for category in categories:
        if category['id'] == args['parent_id'] and (category['id'] not in [1]):
            del category['parent_id']
            category_parent.append(category)
    
    return category_parent