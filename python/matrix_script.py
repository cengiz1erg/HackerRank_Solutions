#!/bin/python3

import math
import os
import random
import re
import sys

x,y = list(map(int,input().split()))
rows =[input() for i in range(x)]
text = "".join([row[i] for i in range(y) for row in rows])
pattern = r'([A-Za-z0-9])[!@#$%&\s]+(?=[A-Za-z0-9])'
text = re.sub(pattern,r'\1 ', text)
print(text)
