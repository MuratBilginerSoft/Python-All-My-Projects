# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:14:53 2020

@author: mrt_b

1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.

"""

for i in range(1,101):
    if i % 3 != 0:
        continue
    else:
        print(i)