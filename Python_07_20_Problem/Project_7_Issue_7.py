"""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

Vize1 toplam notun %30'una etki edecek.

Vize2 toplam notun %30'una etki edecek.

Final toplam notun %40'ına etki edecek.


Toplam Not >=  90 -----> AA

Toplam Not >=  85 -----> BA

Toplam Not >=  80 -----> BB

Toplam Not >=  75 -----> CB

Toplam Not >=  70 -----> CC

Toplam Not >=  65 -----> DC

Toplam Not >=  60 -----> DD

Toplam Not >=  55 -----> FD

Toplam Not <  55 -----> FF

"""

Score1 = float(input("Vize 1 Notunu Giriniz: "))
Score2 = float(input("Vize 2 Notunu Giriniz: "))
FinalScore = float(input(" Final Notunu Giriniz: "))

TotalScore = (Score1 * 0.3) + (Score2 * 0.3) + (FinalScore * 0.4)

if TotalScore >= 90:
    print("Total Score: {0} Geçme Notunuz: AA".format(TotalScore))
elif TotalScore < 90 and TotalScore >= 85:
     print("Total Score: {0} Geçme Notunuz: BA".format(TotalScore))
elif TotalScore < 85 and TotalScore >= 80:
     print("Total Score: {0} Geçme Notunuz: BB".format(TotalScore))
elif TotalScore < 80 and TotalScore >= 75:
     print("Total Score: {0} Geçme Notunuz: CB".format(TotalScore))
elif TotalScore < 75 and TotalScore >= 70:
     print("Total Score: {0} Geçme Notunuz: CC".format(TotalScore))
elif TotalScore < 70 and TotalScore >= 65:
     print("Total Score: {0} Geçme Notunuz: DC".format(TotalScore))
elif TotalScore < 65 and TotalScore >= 60:
     print("Total Score: {0} Geçme Notunuz: DD".format(TotalScore))
elif TotalScore < 60 and TotalScore >= 55:
     print("Total Score: {0} Geçme Notunuz: FD".format(TotalScore))
elif TotalScore < 55:
     print("Total Score: {0} Geçme Notunuz: FF".format(TotalScore))
