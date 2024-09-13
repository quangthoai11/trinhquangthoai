# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 22:13:38 2024

@author: Admin
"""

numbers = [num for num in range(2020, 3839) if num % 9 == 0]
print('\t'.join(map(str, numbers)))