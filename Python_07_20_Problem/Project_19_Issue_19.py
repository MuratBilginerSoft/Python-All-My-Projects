# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 23:33:00 2020

@author: mrt_b

Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

"""

birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

Numb = input("İki Basamaklı Bir Sayı Giriniz: \n")

if len(Numb) == 2:
    
    if int(Numb[0]) != 0:
    
        print("{} >>> {}".format(Numb, str(onlar[int(Numb[0])]) + str(birler[int(Numb[1])])))
    else:
        print("2 Basamaklı Bir Sayı Girmediniz")
else:
    print("2 Basamaklı Bir Sayı Girmediniz")
        