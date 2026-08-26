# Importing in python is the process of loading code from a python module into the current script

import math
result = math.sqrt(9)
print(result) 

# From Keyword - 
from math import sqrt,pi
result = sqrt(9)*pi
print(result)

# Importing Everything -
from math import *
result = sqrt(9)
print(result)
print(pi)

# as keyword -
import math as m
result = m.sqrt(9)
print(result)
print(m.pi)

# dir function - 
import math
print(dir(math))
print(math.cos)
print(type(math.cos))