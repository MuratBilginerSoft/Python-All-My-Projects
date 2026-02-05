# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:37:19 2020

@author: mrt_b

1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).

"""

def MükemmelSayıBul(Numb): 
    
    toplam = 0
    
    for i in range(1,Numb):
        if Numb % i == 0:
            toplam+=i
            print("Bölen: " + str(i) + " Toplam: " + str(toplam) + "\n")

    if toplam == Numb:
        print("{0} Bir Mükemmel Sayıdır".format(Numb))
    else:
        print("{} Bir Mükemmel Sayı Değildir".format(Numb))


Numb1 = int(input("Bir Sayı Giriniz: "))

MükemmelSayıBul(Numb1)