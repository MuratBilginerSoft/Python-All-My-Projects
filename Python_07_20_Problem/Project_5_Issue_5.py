""" 
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

Beden Kitle İndeksi: Kilo / Boy(m) * Boy(m)

BKİ 18.5'un altındaysa -------> Zayıf

BKİ 18.5 ile 25 arasındaysa ------> Normal

BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

BKİ 30'un üstündeyse -------------> Obez  

""" 

import time as tm

height = float(input("Boyunuzu Giriniz(m): "))
weight = float(input("Kilonuzu Giriniz(kg): "))

print("\n")

endex = weight / (height ** 2)

tm.sleep(3)

print("Beden Endex'in:",endex)

print("\n")


if endex < 18.5:
    print("Doktorunuzun Bildirimi: Zayıfsınız")
elif endex >= 18.5 and endex < 25:
    print("Doktorunuzun Bildirimi: Normal")
elif endex >= 25 and endex < 30:
    print("Doktorunuzun Bildirimi: Fazla Kilolu")
elif endex >= 30:
    print("Doktorunuzun Bildirimi: Obez")
else:
    print("Hatalı Değerler Girdiniz")

