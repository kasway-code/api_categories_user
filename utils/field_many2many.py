import ast

def field_many2many(args, name):
        try:
            args[name] = ast.literal_eval(args[name])
        except:
            args[name] = None
            manies = None

        if args[name]  != None:
            manies = []
            for many in args[name] :
                manies.append(many)
            manies = [(6,0,manies)]

        return manies