import pandas as pd
import json

def get_dataAndTotal(data, limit, offset):
    data = pd.DataFrame(data)
    total = len(data)
    data = data.iloc[offset: offset + limit]
    data = data.to_json(orient = 'records')
    data = json.loads(data)
    return data, total