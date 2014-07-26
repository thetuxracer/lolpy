import sys
import string
import random
from time import gmtime, strftime

def open_dev_random(file):
    # print file.read()
    # print os.urandom

    # for i in xrange(100000):
    #     sys.stdout.write(random.choice(string.letters))

    while True:
      # print '1'
      for i in xrange(100):
        sys.stdout.write(random.choice(string.letters))
      # print '\n'  
      print strftime("%Y-%m-%d %H:%M:%S", gmtime())  
      print 'Generating'

dev_random = open('/dev/urandom')

open_dev_random(dev_random)

