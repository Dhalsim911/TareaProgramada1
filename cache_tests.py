#!/usr/bin/python


import sys
import math
from random import randint
# check the integrity of the arguments
#if (len(sys.argv) < 4):
#    print "!!!Invalid number of arguments!!!"
#    sys.exit()
#asoc = sys.argv[1]
#c_size = sys.argv[2]
#b_size = sys.argv[3]

for arg1 in ( "direct", "2-way", "4-way"):
    for arg2 in (512, 1024, 2048, 4096):
        for arg3 in (16, 32, 64, 128):
            asoc = arg1
            c_size = arg2
            b_size = arg3

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
                print
            elif (asoc == "2-way"):
                sets = b_num / 2
                set_size = 2
                print
            else:
                sets = b_num / 4
                set_size = 4
                print

            print asoc, c_size, b_size

            offset = int(math.log(float(b_size),2))
            index = int(math.log(float(sets),2))
            #print " index", index
            cache = [[0 for x in range(set_size)] for x in range(b_num/set_size)]
            print cache
            hit  = 0
            miss = 0

            mask = 1
            for i in range(0, index-1):
                mask = 1 + mask*2

            #print "mask is",mask
            for line in open('aligned.trace'):
            #    print line
                data = line.split()
            #    print "     numer", bin(int(data[0], 16))
            #    print "offset", offset
                tag = int(data[0], 16) #still not the tag
                for i in range (0, offset): #delete the offset form the read
                    tag = (tag / 2)
            #    print "new number", bin(tag)
                read_index = tag & mask     #extract the index
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
                    if (cache[read_index][way] == tag):
                        hit = hit + 1
                    elif (way == set_size-1): #we read all the set and can't fint the tag
                        miss = miss + 1
                        cache[read_index][randint(0,set_size-1)] = tag #random associativity

            print "misses: ",miss, "hits: ", hit
