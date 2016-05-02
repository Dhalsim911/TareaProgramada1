#!/usr/bin/python
from lib import cache
import matplotlib.pyplot as plt

x = [0]*16
y = [0]*16
i = 0
#print x, y
for arg2 in (512, 1024, 2048, 4096):
	for arg3 in (16, 32, 64, 128):
		asoc = "direct"
		c_size = arg2
		b_size = arg3
		
		(hits, miss) = cache.cache(asoc, c_size, b_size)
		print "Misses:", miss, "Hits:", hits
		miss = miss/1.0
		hits = hits/1.0
		total = miss + hits
		print total
		percent = (miss*100)/total
		print "Porcentaje:", percent
		x[i]=arg3
		y[i]=percent
		i = i + 1
print x, y
plt.plot(x[0],y[0], x[1],y[1], x[2],y[2], x[3],y[3], marker='x', linestyle=':', color='b', label="Cache de 512")
plt.plot(x[4],y[4], x[5],y[5], x[6],y[6], x[7],y[7], marker='o', linestyle='-', color='g', label="Cache de 1024")
plt.plot(x[8],y[8], x[9],y[9], x[10],y[10], x[11],y[11], marker='*', linestyle='--', color='r', label="Cache de 2048")
plt.plot(x[12],y[12], x[13],y[13], x[14],y[14], x[15],y[15], marker='^', linestyle='-.', color='c', label="Cache de 4096")
plt.axis([0,130, 0,100])
plt.xlabel('Block Size (B)')
plt.ylabel('Miss Rate (%)')
plt.grid(True)
plt.show()
#		plt.plot(arg3, percent, 'ro')
#		plt.axis([10,130, 0,100])
#		plt.xlabel('Block Size')
#		plt.ylabel('Miss Rate (%)')
#		plt.hold(True)
#		plt.draw()
#	plt.show()
