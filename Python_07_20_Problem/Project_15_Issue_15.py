# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:18:51 2020

@author: mrt_b

1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.

"""

liste = [0]


for i in range(1,101):
    if i % 2 == 0:
        liste.append(i)


print(liste)