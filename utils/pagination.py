def page(pag, limit, offset,amount, args = None):
        if (limit != None) or (offset != None):
            limit  = 1000000 if limit  == None else limit
            offset = 0 if offset == None else offset
            return limit, offset
        elif args!= None:
            pag = args['page']
            limit = amount if pag != None else 10000
            offset = amount*(pag-1) if pag != None else 0
            return limit, offset 
        else:
            limit = amount if pag != None else 10000
            offset = amount*(pag-1) if pag != None else 0
            return limit, offset 