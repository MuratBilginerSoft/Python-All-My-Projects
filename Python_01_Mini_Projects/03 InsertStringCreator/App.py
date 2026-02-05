
tableField = "FirmaUnvanı,VergiDairesi,VergiNumarası,Adres,Telefon,Eposta,YetkiliAdı,KuruluşTürü,FirmaKuruluşŞekli"

formFieldName = "companyName,taxOffice,taxNumber,address,phone,email,authorizedName,establishmentType,establishmentForm"

tableField = input("Enter table fields: ")
formField = input("Enter form fields: ")

tableFieldList = tableField.split(",")
formFieldList = formField.split(",")

queryStr = ""

fieldList = zip(tableFieldList, formFieldList)

for x,y in fieldList:
    queryStr = queryStr + x + f"={y}, "

queryStr = queryStr + f"Değitiren = userId"

print(queryStr)