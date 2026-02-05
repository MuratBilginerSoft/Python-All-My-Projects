# Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

# Hipotenüs Formülü: a^2 + b^2 = c^2

import time as tm

angle1 = float(input("Üçgenin 1. Dik Açısını Giriniz: "))
angle2 = float(input("Üçgenin 2. Dik Açısını Giriniz: "))

print("Hipotenüs Hesaplanıyor...\n")

tm.sleep(3)

hipotenus = (angle1**2 + angle2 ** 2) ** 0.5

print("Hipotenus: ",hipotenus)