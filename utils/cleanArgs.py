def clean_args(args):
            original = args
            filtered = {k: v for k, v in args.items() if v is not None}
            args.clear()
            args.update(filtered)
            try : 
                id_ = args['id']
                del args['id']
                return id_, dict(args)
            except:
                return dict(args)