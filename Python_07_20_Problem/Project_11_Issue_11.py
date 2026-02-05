# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:34:53 2020

@author: mrt_b

Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4

"""

numb = int(input("Kontrol Edilecek Sayıyı Giriniz: "))

basamak = len(str(numb))

print("Basamak Sayısı: " + str(basamak))

sayı = str(numb)

toplam = 0

for i in sayı:
    toplam += pow(int(i),basamak)
    print("Basamak Değeri: " + str(i) + " Toplam: " + str(toplam))


if numb == toplam:
    print("{} Bir Armstrong Sayıdır".format(numb))
else:
    print("{} Bir Armstrong Sayı Değildir".format(numb))