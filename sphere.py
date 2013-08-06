import sys

args = sys.argv[1:]
x = [float(i) for i in args]

s0 = 0.0
for i in xrange(len(x)):
    s0 += x[i]*x[i]
print s0
