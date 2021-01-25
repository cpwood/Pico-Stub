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
    
    stubber.clean()
    stubber.create_all_stubs()
    stubber.report()

countdown()
