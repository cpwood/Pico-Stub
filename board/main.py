import time
from createstubs import Stubber

def countdown():
    for i in range(5, 0, -1):
        print('start stubbing in {}...'.format(i))
        time.sleep(1)

    stubber=Stubber()

    # Add Pico module
    stubber.add_modules(['rp2'])

    # Remove ujson since we've provided a pollyfill
    stubber.modules.remove('ujson')

    # Remove since we've got a frozen version with
    # __getitem__ and __setitem__ defined.
    stubber.modules.remove('array')
    
    stubber.clean()
    stubber.create_all_stubs()
    stubber.report()

countdown()
