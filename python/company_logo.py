#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    letter_counter_dict = dict()
    s = input()
    for i in s:
        if i not in letter_counter_dict:
            letter_counter_dict[i] = 1
        else:
            letter_counter_dict[i] += 1
    sorted_dict_by_count = sorted(letter_counter_dict.items(), key = lambda x: (-x[1], x[0]))
    liste = [sorted_dict_by_count[x] for x in range(3)]
    
    for pair in liste:       
        print(pair[0], end= " ")
        print(pair[1])
        
