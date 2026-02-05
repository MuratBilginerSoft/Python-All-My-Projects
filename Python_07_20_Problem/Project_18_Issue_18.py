# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 23:05:30 2020

@author: mrt_b

Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;

http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok

"""

Ek1 = 1
Ek2 = 1

Numb1 = int(input("Birinci Sayıyı Giriniz: "))
Numb2 = int(input("İkinci Sayıyı Giriniz: "))

print("{} Tüm Bölenleri\n".format(Numb1))


while True:
    
    if Numb1 > 1:
        
        for j in range(2, Numb1+1):
        
            if Numb1 % j == 0:
                Ek1 *= j
                Numb1 = Numb1 // j
                print(j)
                break
    else: 
        break

print("{} Tüm Bölenleri\n".format(Numb2))


while True:
    
    if Numb2 > 1:
        
        for j in range(2, Numb2+1):
        
            if Numb2 % j == 0:
                Ek2 *= j
                Numb2 = Numb2 // j
                print(j)
                break

    else:
        break

TotalEk = Ek1 * Ek2

print("En Küçük Ortak Kat: {}".format(TotalEk))