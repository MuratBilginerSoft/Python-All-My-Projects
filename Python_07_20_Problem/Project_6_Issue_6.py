# Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

Numb1 = int(input("1. Sayıyı Giriniz: "))
Numb2 = int(input("1. Sayıyı Giriniz: "))
Numb3 = int(input("1. Sayıyı Giriniz: "))

if Numb1 > Numb2 and Numb1 > Numb2:
    print("Girilen Sayıların En Büyüğü: {}".format(Numb1))
elif Numb2 > Numb1 and Numb2 > Numb3:
    print("Girilen Sayıların En Büyüğü: {}".format(Numb2))
elif Numb3 > Numb1 and Numb3 > Numb2:
    print("Girilen Sayıların En Büyüğü: {}".format(Numb3))
else:
    print("Hatalı Değerler")



