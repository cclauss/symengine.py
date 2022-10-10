from __future__ import print_function
from timeit import default_timer as clock
from sage.all import var
var("x y z")
f = (x**y + y**z + z**x)**100
print(f)
t1 = clock()
g = f.expand()
t2 = clock()
print("Total time:", t2-t1, "s")
