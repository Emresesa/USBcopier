
import shutil
import os

filetype=raw_input("Dosyanin adini veya uzantisini giriniz")
#sistemden username'i almak
nuser=os.path.expanduser('~')
nuser=os.path.split(nuser)[-1]
#Usb lerin bulundugu klasorun ve Kopyalanacak klasor'un path i
usbway="/run/media/%s"%(nuser)
destway="/home/%s/Belgeler/UsbF"%nuser
#Farkli USB lerin listesi
usbarr=os.listdir(usbway)
#Her USB klasorune ozel path olusturulmasi
for i,k in enumerate(usbarr):
    dirway=usbway+"/"+usbarr[i]
    filearr=os.listdir(dirway)
#Her USB deki uzantisi belirtilen dosyanin kopyalanmasi
    for y,x in enumerate(filearr):
        if filearr[y].endswith('filetype'):
            filename=dirway+"/"+filearr[y]
            shutil.copy(filename,destway)

#USb klasorlerinin ekrana yazilmasi
print "USB drive(s) : %s" % usbarr
print "islem yapildi"
