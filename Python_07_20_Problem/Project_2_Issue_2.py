# Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

# Beden kitle indeksi, vücut ağırlığının (kg olarak),boy uzunluğunun (metre cinsinden) karesine bölünmesiyle hesaplanır.

import time as tm

height = float(input("Boyunuzu Giriniz(m): "))
weight = float(input("Kilonuzu Giriniz(kg): "))

endex = weight/(height**2)

print("\nVücut Kitle Endeksiniz Hesaplanıyor...\n")

tm.sleep(3)

print("Vücut Kitle Endeksiniz:{0} ".format(endex))

# Önemli Not: Kullanılan time kütüphanesi zaman işlemlerini yapmak için üretilmiş bir kütüphanedir. Kodları 3 sn bekletip devap etmek için bu kütüphaneye ihtiyaç duyduk.

# Kitle endeksi hesaplanırken bir hesaplama işlemi yapılıyor havası vermek için o adımda kodları 3 sn durdurduk. bunu tm.sleep(3) koduyla yaptık.

# time.sleep(sec) çalışan kodların kaç sn durdurulacağını belirler.