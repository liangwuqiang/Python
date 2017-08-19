import virtkey
# import time
def simulate():
    #while 1:
    v = virtkey.virtkey()
    print v.press_unicode(ord('a'))
        #time.sleep(3)
        #v.press_unicode(ord("a"))
        #v.release_unicode(ord("a"))
        #v.press_keysym(65363)
        #v.release_keysym(65363)
simulate()