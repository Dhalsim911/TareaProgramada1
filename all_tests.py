#!/usr/bin/python
from lib import cache

file = open('log', 'w')

for arg1 in ( "direct", "2-way", "4-way"):
    for arg2 in (512, 1024, 2048, 4096):
        for arg3 in (16, 32, 64, 128):
            asoc = arg1
            c_size = arg2
            b_size = arg3

            (hits, miss) = cache.cache(asoc, c_size, b_size)
            print "misses: ",miss, "hits: ", hits
            # data = (asoc, c_size, b_size, miss, hits)
            # for i in data:
            #     file.write(i)
            file.write(asoc + " " + str(c_size) + " " + str(b_size) + " " + str(miss) + " " + str(hits))
            file.write("\n")
