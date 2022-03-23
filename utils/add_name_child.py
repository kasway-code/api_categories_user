import pandas as pd
import json 

def add_name_child(models, db,uid,password, data):
    data = pd.DataFrame(data)
    def add_name(child_ids):
        data_child = models.execute_kw(
            db,uid,password, 'product.category',
            'search_read',
            [[['id', 'in', child_ids]]],
            {
                'fields': ['name', 'id']
            }
        )
        return data_child

    data['child_id'] = data['child_id'].apply(add_name)

    data = data.to_json(orient = 'records')
    data = json.loads(data)
    
    return data
