import subprocess
import os

folderPath = os.path.join("C:\\","AppStart")

if not os.path.exists(folderPath):
    os.mkdir(folderPath)

appFilePath = os.path.join(folderPath,"Apps.txt")

# Dosya yolunun var olup olmadığını kontrol edin
if not os.path.exists(appFilePath):
    # Dosya yolu yoksa dosyayı oluşturun
    with open(appFilePath, 'w') as f:
        pass

# Dosyayı okumak için 'r' (read) modunda açın
with open(appFilePath, 'r') as f:
    # Dosya içeriğini satır satır okuyun
    lines = f.readlines()

appList = []

for line in lines:
    appList.append(line.strip())

print(appList)

for program in appList:

    print("Starting: " + program)

    subprocess.Popen([program])

print("Done")