# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:05:20 2020

@author: mrt_b

Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. Bu fonksiyon, eğer sayı çift ise return ile bu değeri dönsün. Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatsın. Daha sonra, içinde çift ve tek sayılar bulunduran bir liste tanımlayın ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın.

"""

def ciftmi(sayı):
    if sayı % 2 == 0:
        return sayı
    else:
        raise ValueError("Girilen Sayı Tek")

liste = [12,34,56,75,32,4,3,65,89,21]

for i in liste:
    try:
       print(ciftmi(i))
    except ValueError:
        print("Sayı Tekti")
