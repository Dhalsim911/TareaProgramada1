#!/usr/bin/python

import sys
import math
from random import randint

def cache (asoc, c_size, b_size):
    if (asoc not in ("direct", "2-way", "4-way")):
        print "Invalid associativity name, valid names: direct, 2-way, 4-way"
        sys.exit()

    c_size = int(c_size)
    b_size = int(b_size)

    if((c_size & (c_size -1)) != 0):
	    print "Invalid cache size, use a base 2 number"
	    sys.exit()

    if((b_size & (b_size -1)) != 0):
	    print "Invalid block size, use a base 2 number"
	    sys.exit()

    b_num = c_size / b_size

    #select the associativity
    if (asoc == "direct"):
        sets = b_num
        set_size = 1
    elif (asoc == "2-way"):
        sets = b_num / 2
        set_size = 2
    else:
        sets = b_num / 4
        set_size = 4

    print "Running test for: ", asoc, c_size, b_size

    offset = int(math.log(float(b_size),2))
    index = int(math.log(float(sets),2))
    cache = [[0 for x in range(set_size)] for x in range(b_num/set_size)]
    print cache
    hit  = 0
    miss = 0
    mask = 0
    #This mas will be used to extract the index
    for i in range(index):
        mask = 1 + mask*2

    for line in open('aligned.trace'):
        data = line.split()
        tag = int(data[0], 16) #still not the tag
        for i in range (offset): #delete the offset from the read
            tag = (tag / 2)
        read_index = tag & mask     #extract the index
        for i in range (index): #delete the index from the read
            tag = (tag / 2) #now we have only the tag in $tag

    #no-write allocate and write through, if we have a hit we do nothing to the cache,
    #(that's because we aren't working with data)
    #if we have a miss we copy the memory direction in the cache

        for way in range (set_size):
            if (cache[read_index][way] == tag):
                hit = hit + 1
                break
            elif (way == set_size-1): #we read all the set and can't fint the tag
                miss = miss + 1
                cache[read_index][randint(0,set_size-1)] = tag #random associativity

    return (hit, miss)
