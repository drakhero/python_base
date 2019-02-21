#_*_ coding: utf-8 _*_
from __future__ import unicode_literals
import datetime as dt
import numpy as np

begin = dt.datetime.now()
n = 100000

A,B = [],[]
for i in range(n):
    A.append(i ** 2)
    B.append(i ** 3)

C = []
for a,b in zip(A,B):
    C.append(a + b)
time = (dt.datetime.now() - begin).microseconds
print(time)

begin = dt.datetime.now()
A,B = np.arange(n) ** 2,np.arange(n) ** 3
C = A + B
time = (dt.datetime.now() - begin).microseconds
print(time)
