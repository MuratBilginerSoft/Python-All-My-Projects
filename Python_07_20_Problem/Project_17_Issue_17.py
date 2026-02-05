# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 22:43:19 2020

@author: mrt_b

Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;

http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok

"""

Liste1 = list()
Liste2 = list()

Numb1 = int(input("Birinci Sayıyı Giriniz: "))
Numb2 = int(input("İkinci Sayıyı Giriniz: "))


print("{} Tüm Bölenleri".format(Numb1))

for i in range(1,Numb1+1):
    if Numb1 % i == 0:
        Liste1.append(i)
        print(i)
        

print("{} Tüm Bölenleri".format(Numb2))

for i in range(1, Numb2+1):
    if Numb2 % i == 0:
        Liste2.append(i)
        print(i)

print("{} ve {} Ortak Bölenleri".format(Numb1,Numb2))

for i in Liste1:
    for j in Liste2:
        if i == j:
            print(i)

