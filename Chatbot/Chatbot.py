Chatbot

print("Selamunaleyküm")

ad = str(input("Adın ne:"))
import random
import time

liste0 = ["Güzel isimmiş","Hmm fena değilmiş","Gayet şık bir isim","Çok kullanılan bir isim","Tarihi bir isim","Garipmiş"]
liste1 = ["oo severiz","Valla güzel yer","Memleketimin her yeri güzel"]
liste2 = ["Ooo Geleceğin mesleği","Fena değil","Nasıl iş bulabilirsin ki onla","İŞ bulunabilir"]
liste3 = ["Kolaya kaçma","Ooo güzel dil","Zor severim diyosun","Bende severim"]
liste4 = ["Hmm","bu burçta tanıdığım çok az insan var","agrasifim diyosun","hiç beklemiyodum","dediklerine göre çok utangaçmışsın"]
liste5 = ["1","2","3","4","5","6","7","8","9","10"]

if ad =="sanane":
    print("Oğlum bi soru soruyoruz sana adam gibi cevap ver!")

else:
    print(random.sample(liste0, 1))


yas = int(input("Yaş Kaç(Lütfen sayı ile giriş yapın):"))

if yas <= 0:
    print("!Lütfen geçerli bir yaş giriniz!")


elif 4 <= yas <= 12:
    print("Çocuk")

elif 18 <= yas <= 50:
    print("Büyüğümsün")

elif 50 <= yas <= 60:
    print("Hafiften çökmüş")

elif 61 <= yas <= 90:
    print("Yaşlı")

elif 91 <= yas <= 150:
    print("ÖLmeyi unutmuş")

elif 301 <= yas <= 400:
    print("Tarihi kalıntı")

elif 1 <= yas <= 3:
    print("Bebe")

elif 13 <= yas <= 16:
    print("Ergen bu ya")


elif yas == 17:
    print("Ergenlikten çıkmak üzeresin")

else:
    print("!Lütfen geçerli bir yaş giriniz!")
#----------------------------------------------------------------------------------------

memleket = str(input("Senin memleket nere?:"))

if memleket == "kars":
    print("hemşeri çıktık ya")

elif memleket =="sanane":
    print("Oğlum bi soru soruyoruz sana adam gibi cevap ver!")

else:
    print(random.sample(liste1,1))

#----------------------------------------------------------------------------
bolum =  str(input("Hangi Bölümde okuyosun/okudun?(Bölümün yoksa 'yok' yaz.):"))


if bolum =="yok":
    meslek =str(input("işsiz misin?(evet/hayır):"))

    if meslek == "evet":
        print("Okumak önemli işte")

    elif meslek == "hayır":
        meslek2= str(input("E söyle o zaman:"))
        print(random.sample(liste2, 1))

elif bolum == "bilişim":
    print("Geleceğim mesleği valla")

elif bolum == "bilişim":
    print("Geleceğim mesleği valla")


elif bolum =="sanane":
    print("Oğlum bi soru soruyoruz sana adam gibi cevap ver!")

else:
    print(random.sample(liste2,1))
#------------------------------------------------------------

dil = str(input("En sevdiğin progrmlama dili ne? benimki Python(programlama bilmiyorsan 'bilmiyorum'yaz):"))

if dil == "benimde":
    print("valla sende ağzının tadını biliyon ")

elif dil == "sanane":
    print("Oğlum bi soru soruyoruz sana adam gibi cevap ver!")
elif dil == "bilmiyorum":
    print("aga be bilmiyon mu... neyse")

else:
    print(random.sample(liste3,1))
#------------------------------------------------------------------------------------

burc = str(input("Ya ben aslında pek inanmam ama bi sorayım. senin burcun neydi?:"))

if burc == "yengeç":
    print("aa benimde")

else:
    print(random.sample(liste4,1))

print("Tüm Sorularımı cevepladın şimdi aklından 1'den 10'a kadar bi sayı tut")
time.sleep(5)
durum2 = str(input("Tuttun mu(tuttum/hayır)..."))

if durum2 == "tuttum":
        time.sleep(3)
        print(random.sample(liste5, 1, ))

elif durum2 == "hayır":
    print("bekliyorum...")
    time.sleep(4)
    durum2 = str(input("Tuttun mu(tuttum/hayır)..."))

    if durum2 == "tuttum":
        print(random.sample(liste5, 1, ))

    elif durum2 == "hayır":
        print("bekliyorum...")
        time.sleep(4)
        durum2 = str(input("Tuttun mu(tuttum/hayır)..."))

        if durum2 == "tuttum":
            print(random.sample(liste5, 1, ))

        elif durum2 == "hayır":
            print("bekliyorum...")

soru = str(input("Doğru mu?(evet/hayır)"))

if soru == "evet":
    print("Biliyodum:)")

elif soru == "hayır":
    print("aga bee :,(")

print("Neyse onu boşver şimdi seninle başka bir oyun oynayalım")
time.sleep(5)
print("Şimdi aklından bi sayı tut...")
time.sleep(3)

durum2 = str(input("Tuttun mu(tuttum/hayır)..."))

if durum2 == "tuttum":
    print("tamam şimdi o sayıyı 2 ile çarp")
    time.sleep(3)
elif durum2 == "hayır":
    print("Hadi ama..")
    time.sleep(3)

    durum2 = str(input("Tuttun mu(tuttum/hayır)..."))

    if durum2 == "tuttum":
        print("tamam şimdi o sayıyı 2 ile çarp")
        time.sleep(3)
    elif durum2 == "hayır":
        print("Hadi ama..")
        time.sleep(3)
        durum2 = str(input("Tuttun mu(tuttum/hayır)..."))

        if durum2 == "tuttum":
            print("tamam şimdi o sayıyı 2 ile çarp")
            time.sleep(3)
        elif durum2 == "hayır":
            print("Hadi ama..")


print("Şimdi bulduğun sayıya 10 ekle")
time.sleep(5)


print("Sonra bu sayıyı 2 ye böl")
time.sleep(5)


print("Son olarak tuttuğun sayıdan ilk tuttuğun sayıyı çıkar")
time.sleep(3)


sonuc = str(input("Sonuç 5 mi :)(evet/hayır)"))

if sonuc == "evet":
    print("hahaha basit")
elif sonuc == "hayır":
    print("Yalan söyleme")
time.sleep(3)

print("HER NEYSE DOSTUM SENİNLE SOHBET ETMEK GÜZELDİ.")
time.sleep(3)
print("Hadi bana müsade...")

from tkinter import *

window = Tk()

window.title("main.py")

window.mainloop()