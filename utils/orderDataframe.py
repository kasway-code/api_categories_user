import pandas as pd
import json 

def dataframe(col, data):
        sales = pd.DataFrame(data)
        sales = sales.sort_values(by = col, ascending = True)
        sales = sales.to_json(orient= 'records')
        sales = json.loads(sales)
        return sales