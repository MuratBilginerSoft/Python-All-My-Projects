import pandas.io.sql
import pandas as pd
import pymssql
import os
from sqlalchemy import create_engine


UserFolderWindows = os.getcwd() + "\\assets\\ExcelFile\\"

ExcelFileName = input('Excel Dosyasının Adını Giriniz: ')
SheetName = input("Excel Sheet İsmini Giriniz: ")
TableName = input("Oluşturulacak Tablo İsmini Giriniz: ")

ServerName = input("Server Name Ya da Ip Bilginizi Giriniz: ")
UserName = input("Veritabanı Kullanıcı İsminizi Giriniz: ")
Password = input("Veritabanı Şifrenizi Giriniz: ")
DatabaseName = input("Verinin Yazılacağı Veritabanı İsmini Giriniz: ")

SourceFile = UserFolderWindows +  ExcelFileName

ClusteredData = pd.read_excel(SourceFile, sheet_name=SheetName)

mssql_str = f'mssql+pymssql://{UserName}:{Password}@{ServerName}/{DatabaseName}'
cnx = create_engine(mssql_str)
ClusteredData.to_sql(TableName, con=cnx, index=False, if_exists='replace')

