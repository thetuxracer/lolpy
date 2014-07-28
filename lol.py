import sys
import string
import random
from time import time, sleep, gmtime, strftime
from random import randrange

def open_dev_random():
    # print file.read()
    # print os.urandom

    # for i in xrange(100000):
    #     sys.stdout.write(random.choice(string.letters))
    foo = ''

    while True:
      # print '1'
      for i in xrange(100):
        foo += random.choice(string.letters)
      # print '\n'  
      current_date = strftime("%Y-%m-%d %H:%M:%S", gmtime())  
      # print 'Generating'
      print "[%s] Generating %s" % (current_date, foo)
      foo = ''
      sleep(randrange(0, 3))

 
# dev_random = open('/dev/urandom')

open_dev_random()

