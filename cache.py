#!/usr/bin/python

import sys
import math
from random import randint
# check the integrity of the arguments
if (len(sys.argv) < 4):
    print "!!!Invalid number of arguments!!!"
    sys.exit()
asoc = sys.argv[1]
c_size = sys.argv[2]
b_size = sys.argv[3]
if (asoc == "direct" or "2-way" or "4-way"):
    print
else:
    print "Invalid associativity name, valid names: direct, 2-way, 4-way"
    sys.exit()

b_num = int(c_size) / int(b_size)

#select the associativity
if (asoc == "direct"):
    sets = b_num
    set_size = 1
    mask = 1
    print
elif (asoc == "2-way"):
    sets = b_num / 2
    set_size = 2
    mask = 3
    print
else:
    sets = b_num / 4
    set_size = 4
    mask = 7
    print

print asoc, c_size, b_size

offset = int(math.log(float(b_size),2))
index = int(math.log(float(sets),2))
cache = [[0 for x in range(set_size)] for x in range(b_num)]
print cache
hit  = 0
miss = 0

for line in open('aligned.trace'):
#    print line
    data = line.split()
#    print "     numer", bin(int(data[0], 16))
#    print "offset", offset
    tag = int(data[0], 16) #still not the tag
    for i in range (0, offset): #delete the offset form the read
        tag = (tag / 2)
#    print "new number", bin(tag)
    read_idex = tag & 3     #extract the index
#    print "read index", read_idex
    for i in range (0, index): #delete the index from the read
        tag = (tag / 2)
    #now we have only the tag in $tag
#    print "new number", bin(tag)
#    print "index is",index
#    print "sets is", sets

#no-write allocate and write through, if we have a hit we do nothing to the cache,
#(that's because we are't working with data)
#if we have a miss we copy the memory direction in the cache

    for way in range (0, set_size):
#        print "way is ",way
        if (cache[read_idex][way] == tag):
            hit = hit + 1
        elif (way == set_size-1): #we read all the set and can't fint the tag
            miss = miss + 1
            cache[read_idex][randint(0,set_size-1)] = tag #random associativity

print "misses: ",miss, "hits: ", hit
