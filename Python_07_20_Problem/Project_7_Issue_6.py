# Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

# list ile çözümü

Numbers = list()

Numbers.append(int(input("1. Sayıyı Giriniz: ")))
Numbers.append(int(input("2. Sayıyı Giriniz: ")))
Numbers.append(int(input("3. Sayıyı Giriniz: ")))

Numbers.sort()

Numbers.reverse()

print("Girilen Sayıların En Büyüğü: {}".format(Numbers[0]))

