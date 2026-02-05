# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:50:33 2020

@author: mrt_b

1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.

"""

boyut = int(input("Çarpım Tablosu Boyutunu Giriniz: "))

for i in range(1,boyut+1):
    print("\n {} ler/lar \n".format(i))
    for j in range(1,11):
        print("{0} * {1} = {2}".format(i,j,i*j))