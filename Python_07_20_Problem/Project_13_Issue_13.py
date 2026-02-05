# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:01:09 2020

@author: mrt_b

Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.

"""
toplam = 0

while True:
    val = input("Bir Sayı Giriniz:(Exit:Q) ")
    
    if val == "Q" or val == "q":
        print("Toplam:{} ".format(toplam)) 
        break
    else:
        toplam += int(val)