import sys
from math import cos, pi

args = sys.argv[1:20]
x = [float(i) for i in args]

s0 = 0.0
for i in xrange(len(x)):
    t = x[i]
    s0 += t*t - 10*cos(2.0 * pi * x[i])
print s0 + len(x)*10
