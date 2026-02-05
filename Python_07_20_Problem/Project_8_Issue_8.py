"""

Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;

abs(-4)
4
abs(5)
5

"""

print("""*************************
      
  Geometrik Şekil Bulma Programı
      
*************************""")

Shape = input("Bulmak İstediğiniz Şekli Giriniz:( Üçgen / Dörtgen )")

durum1 = False
durum2 = False

if Shape == "Üçgen":
    
    kenar1 = float(input("Birinci Kenarı Giriniz: "))
    kenar2 = float(input("İkinci  Kenarı Giriniz: "))
    kenar3 = float(input("Üçüncü  Kenarı Giriniz: "))
    
    durum1 = kenar1 < kenar2+kenar3 and kenar2 < kenar1 + kenar3 and kenar3 < kenar1 + kenar2
    
    durum2 = kenar1 > abs(kenar2 - kenar3) and kenar2 > abs(kenar1 - kenar3) and kenar3 > abs(kenar1 - kenar2)
    
    if durum1 and durum2:
        if kenar1 == kenar2 == kenar3:
            print("Girilen Bir Eşkenar Üçgendir")
        elif kenar1 == kenar2 != kenar3 or kenar2 == kenar3 != kenar1 or kenar1 == kenar3 != kenar2:
            print("Girilen Bir İkizkenar Üçgendir")
        else:
            print("Girilen Bir Çeşitkenar Üçgendir")
    else:
        print("Bu Üçgen Çizilemez")
        
        
elif Shapte == "Dörtgen":
    kenar1 = float(input("Birinci  Kenarı Giriniz: "))
    kenar2 = float(input("İkinci   Kenarı Giriniz: "))
    kenar3 = float(input("Üçüncü   Kenarı Giriniz: "))
    kenar4 = float(input("Dördüncü Kenarı Giriniz: "))
    
    if kenar1 == kenar2 == kenar3 == kenar4:
        print("Girilen Şekil Bir Karedir")
    elif (kenar1 == kenar3) and (kenar2 == kenar4):
        print("Girilen Şekil Bir Diktörtgendir")
    else:
        print("Girilen Şekil Bir Çeşitkenar Dörtgendir")
else:
    print("Doğru Bir Geometrik Şekil Girmediniz")
    
    
