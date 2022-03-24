def clean_domains(domains):
        ds = []
        for d in domains :
            try:
                if d[2] != None:
                    ds.append(d)
            except:
                ds.append(d)
        return ds