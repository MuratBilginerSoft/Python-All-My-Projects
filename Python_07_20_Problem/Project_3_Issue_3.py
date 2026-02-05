# Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.

import time as tm

KmPrice = float(input("Aracın Km Başı Yaktığı Ücret:"))
Km = float(input("Araç Kaç Km Gitti: "))

print("Ödeyeceğiniz Ücret Hesaplanıyor...\n")

tm.sleep(3)

TotalPrice = KmPrice * Km

print("Ödemeniz Gereken Ücret:{}".format(TotalPrice))





