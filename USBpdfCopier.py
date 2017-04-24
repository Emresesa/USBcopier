import shutil
import os


filetype=raw_input("pdfleri kopyalamak icin enter a basin")
#filetype=raw_input("Dosyanin adini veya uzantisini giriniz")
#Klasorlerin pathlerini cikaran fonksiyon
def dirpaths(way):
    dirpaths=[]
    for(dirpath,dirnames,filenames) in os.walk(way):
        dirpaths.append(dirpath)
    return dirpaths
#Klasorlerdeki dosyalari kopyalayan fonksiyon
def copier(patharr):
    for y,x in enumerate(patharr):
        filearr=os.listdir(dirP[y])
        for i,x in enumerate(filearr):
            if filearr[i].endswith('.pdf'):
                filename=dirP[y]+"/"+filearr[i]
                shutil.copy(filename,destway)
#sistemden username'i almak
nuser=os.path.expanduser('~')
nuser=os.path.split(nuser)[-1]

#destination ve start pathleri
usbway="/home/%s/Belgeler/Kitaplar"%nuser
#kopyalanacak klasorun check edilmesi yoksa acilmasi
destway= "/home/%s/Belgeler/USBfiles"%nuser
if not os.path.exists(destway):
    os.makedirs(destway)
#destway="/home/%s/Belgeler/KCM"%nuser
#path in cikartilmasi
dirP=dirpaths(usbway)
#dosyalari kopyalayan fonsiyonun cagirilmasi
copier(dirP)


aa=os.listdir(destway)
print "Kopyalanan dosyalarin listesi \n"+ str(aa)
