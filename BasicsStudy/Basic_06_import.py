# coding: utf-8
"""import的使用"""

from math import sqrt
print(sqrt(9))      # 结果：3.0
from math import sqrt as a
print(a(9))         # 结果：3.0
import math
print(math.sqrt(9))  # 结果：3.0
