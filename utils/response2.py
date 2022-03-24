def MessageResponse2(message, data, need_description = False, description = ''):
        if need_description: 
                response = {
                        'response':message,
                        'description': description,
                        'data': data
                }
                        
        else:
                response = {
                        'response':message,
                        'data': data
                }

        return response