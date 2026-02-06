import os
import ctypes

cmd = 'tasklist /FI "STATUS eq RUNNING" /FO CSV /NH'

# Komutu çalıştırıp çıktıyı elde et
output = os.popen(cmd).read()

folderPath = os.path.join("C:\\","AppKill")

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


# Çıktıdaki her satırı işle
for line in output.splitlines():
    # Eğer satır boş ise bir sonraki satıra geç
    if not line:
        continue

    # Satırdaki uygulamanın adını bul
    app_name = line.split(",")[0].strip('"')

    if app_name in appList:

        # Uygulamanın PID'sini bul
        if line.split(",")[1].strip('"').isdigit():

            pid = int(line.split(",")[1].strip('"'))
            # Uygulamayı bul

            handle = ctypes.windll.kernel32.OpenProcess(1, False, pid)
            ctypes.windll.kernel32.TerminateProcess(handle, 0)
            # Handle'ı kapat
            ctypes.windll.kernel32.CloseHandle(handle)