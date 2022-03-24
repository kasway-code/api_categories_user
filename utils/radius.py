from math import acos, cos, sin
import pandas as pd
import json

def radiusFUN(stores, slat, slon):
            try:
                indexs = []
                for index, store in enumerate(stores):
                    elat   = store['latitude']
                    elon   = store['longitude']
                    store['distance'] = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
                stores = pd.DataFrame(stores)
                stores = stores.sort_values(by = 'distance', ascending = True)
                stores = stores.to_json(orient = 'records')
                stores = json.loads(stores)
                return stores

            except:
                for store in stores:
                    store['dist_user_km'] = 0
                return stores