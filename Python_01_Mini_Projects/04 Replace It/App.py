import re

def degistir_html(dosya_adi, baslangic, yeni_deger):
    with open(dosya_adi, 'r') as dosya:
        icerik = dosya.read()

    yeni_icerik = re.sub(rf'{baslangic}.+?"', yeni_deger, icerik)

    with open(dosya_adi, 'w') as dosya:
        dosya.write(yeni_icerik)

# Kullanım örneği
dosya_adi = 'Index.html'
baslangic = 'src="'
yeni_deger = '''src="{{url_for('static', filename='UI/Adeyun/image/Content/image0.jpeg')}}"'''

degistir_html(dosya_adi, baslangic, yeni_deger)