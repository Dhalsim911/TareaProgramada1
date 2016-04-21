#!/usr/bin/python
import sys
from lib import cache

#check the integrity of the arguments
if (len(sys.argv) < 4):
    print "!!!Invalid number of arguments!!!"
    sys.exit()

asoc = sys.argv[1]
c_size = sys.argv[2]
b_size = sys.argv[3]

(hits, miss) = cache.cache(asoc, c_size, b_size)
print "misses: ",miss, "hits: ", hits
