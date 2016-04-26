#!/usr/bin/python
from lib import cache
import matplotlib.pyplot as plt

for arg3 in (16, 32, 64, 128):
	asoc = "direct"
	c_size = 512
	b_size = arg3

	(hits, miss) = cache.cache(asoc, c_size, b_size)
	print "Misses:", miss, "Hits:", hits
	miss = miss/1.0
	hits = hits/1.0
	total = miss + hits
	print total
	percent = (miss*100)/total
	print "Porcentaje:", percent
	plt.plot(arg3, percent, 'ro')
	plt.axis([10,130, 0,100])
	plt.xlabel('Block Size')
	plt.ylabel('Miss Rate (%)')
	plt.hold(True)
	plt.draw()
plt.show()
