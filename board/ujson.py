# Poor man's polyfill for ujson.dumps() since this isn't
# available on the Pico. 

def dumps(obj):
    return repr(obj).replace("'", '"')
