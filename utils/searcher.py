import pandas as pd
import json

def searcher(data, value, limit, offset,col = 'name' ):
        data = pd.DataFrame(data)
        series = data[col].str.upper()
        data = data[series.str.contains(value.upper())]
        data = pd.DataFrame(data)
        total = len(data)
        data = data.iloc[offset: offset + limit]
        data = data.to_json(orient = 'records')
        data = json.loads(data)
        return total, data