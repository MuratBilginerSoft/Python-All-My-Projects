# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:00:05 2020

@author: mrt_b

Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.

liste = ["345","sadas","324a","14","kemal"]

Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın. Bunu yaparken try,except bloklarını kullanmayı unutmayın.

"""

liste = ["345","sadas","324a","14","kemal"]


for i in liste:
    try:
        a = int(i)
        print(a)
    except:
        pass
