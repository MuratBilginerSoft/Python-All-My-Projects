# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:23:28 2020

@author: mrt_b

Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

"""

numb = int(input("Sayı Kontrolü İçin Bir Sayı Giriniz: "))
toplam = 0

for i in range(1,numb):
    if numb % i == 0:
        toplam+=i
        print("Bölen: " + str(i) + " Toplam: " + str(toplam) + "\n")

if toplam == numb:
    print("{0} Bir Mükemmel Sayıdır".format(numb))
else:
    print("{} Bir Mükemmel Sayı Değildir".format(numb))
