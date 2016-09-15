
import sys
print sys.path


from FooClass import FooClass

import numpy
m = 10
xIn = numpy.ones([m])
xOut = numpy.empty([m])

f = FooClass(m)

f.foo(xIn, xOut)

print xIn
print xOut