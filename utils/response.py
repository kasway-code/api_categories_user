import math 

def MessageResponse(message,data,page,total,amount=10,need_description=False,description=''):

    division = math.ceil(total/amount) 

    if need_description: 
        response = {
            'message':message,
            'description': description,
            'post': {
                'data':data,
                'pagination':{
                    'hasPrevPage': True if (page <= (division ) and (page > 1)) else False,
                    'hasNextPage':  True if ((page < (division) and (page >= 1)) ) else False,
                    'prevPage':(page - 1) if (page <= (division ) and (page > 1)) else None,
                    'nextPage': (page +1 ) if ((page < (division) and (page >= 1)) ) else None,
                    'page':page,
                    'perPage': len(data),
                    'totalPages': division
        }}}
    else: 
        response = {
            'message':message,
            'post': {
                'data':data,
                'pagination':{
                    'hasPrevPage': True if (page <= (division ) and (page > 1)) else False,
                    'hasNextPage':  True if ((page < (division) and (page >= 1)) ) else False,
                    'prevPage':(page - 1) if (page <= (division ) and (page > 1)) else None,
                    'nextPage': (page +1 ) if ((page < (division) and (page >= 1)) ) else None,
                    'page':page,
                    'perPage': len(data),
                    'totalPages': division
        }}}

    
    return response