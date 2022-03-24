from .image1920 import photo

def add_photo(args, name):
    try:
        logo = photo(args[name])
    except Exception as error:
        if args[name] == None:
            logo = None 
        elif args[name] != None:
            if "NoneType' object has no attribute 'read'" in str(error):
                logo = False
        else:
            logo = None
    
    return logo