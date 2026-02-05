import uuid

# Ana bilgisayar kimliğine ve geçerli zamana göre bir UUID oluşturalım ilk olarak. Bunu uuid1 ile yapabiliriz.

id = uuid.uuid1()
print(id)

# Bir ad alanı UUID'sinin MD5 karmasını ve bir adı kullanarak bir UUID oluşturalım.

id2 = uuid.uuid3(uuid.NAMESPACE_DNS, 'python')
print(id2)

# Rastgele bir UUID yap

id3 = uuid.uuid4()
print(id3)

# Bir ad alanı UUID'sinin SHA-1 karmasını ve bir adı kullanarak bir UUID oluşturalım.

id4  = uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')
print(id4)

# Bir dizi onaltılık rakamdan bir UUID oluşturalım. (parantezler ve kısa çizgiler yok sayılır)

id5  = uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}')
print(id5)

# Elimizdeki bir UUID'yi standart biçimde bir onaltılık basamak dizisine dönüştürelim.

id6= uuid.uuid4()
print(str(id6))

# Bir UUID için onaltılık değer istiyorsanız, aşağıdakini yapabilirsiniz

id7 = uuid.uuid4().hex
print(str(id7))