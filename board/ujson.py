# Poor man's pollyfill for ujson.dumps() since this isn't
# available on the Pico. Will create single-quoted JSON, but
# we will use prettify.js to turn this into conventional JSON
# later on.

def dumps(obj):
    return repr(obj)
