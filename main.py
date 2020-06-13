

ad=input("Kullanıcı adınızı giriniz:")

sifre=input("Şifrenizi giriniz:")



uzunluk=0 # her bölmede bir bayrak koyacağım =0 diyeceğim şartı sağlarsa 1 olacak ve en son bu şartları kontrol edeceğim şifre doğru olabilecek mi

# 8 karakterden uzun,12 karakterden kisa olup olmadıgını kontrol et

if len(sifre)<8:
    print("Girdiğiniz şifre en az 8,en fazla 12 karakterli olmalıdır.")
if len(sifre)>12:
    print("Girdiğiniz şifre en az 8,en fazla 12 karakterli olmalıdır.")
else:
    uzunluk=1   # uzunluk-->bayrak 1


# buyuk harf kucuk harf icerme durumunu kontrol et

kbd=0   # küçük büyük durumu-->bayrak 2

if (sifre.upper()==sifre):    # sifredeki tum karakterleri hazır fonk.yardımı ile büyüt ve sifreye esit olup olmadigina bak
    print("Şifre en az bir küçük harf içermelidir.")
if(sifre.lower()==sifre):     #sifredeki tum karakterleri hazır fonk.yardımı ile kucult ve sifreye esit olup olmadigina bak
    print("Şifre en az bir büyük harf içermelidir.")
else:
    kbd=1



# rakam ile baslayip bitmeme durumunu kontrol et

rakamlık=0  #-->bayrak 3

rakam = "0123456789"     # python girilenleri string olarak algiladigi icin string bir 'rakam' karakter dizisi olusturdum

for i in range(len(rakam)):         # rakamin uzunluguna kadar git
    if (sifre[0] == rakam[i] or sifre[-1] == rakam[i]):      # sifrenin ilk veya son karakterlerinin 'rakam' karakter dizisindeki herhangi bir elemana esit olup olmadigini kontrol et
        print("Şifre sayı ile başlayıp sayı ile bitemez.")
    else:
        rakamlık=1  #rakam ile baslama bitme-->bayrak 3





# bosluk karakteri icerip icermedigini kontrol et

bosluk=0    # -->bayrak 4


for i in range(len(sifre)):
    if(sifre[i] == " "):
        print("Şifre boşluk karakteri içeremez.")

bosluk=1



# alfanümerik karakter icerip icermedigini kontrol et

alfanümeriklik=0 # -->bayrak 5

kharf="abcdefghijklmnopqrstuvwxyz"
bharf=kharf.upper()   # kucuk harfleri hazir fonk. yardımıyla buyuttum ve bharf karakter dizisi olusturdum
alfanümerik=bharf+kharf+rakam   # alfanümerik:a-z arasındaki harfler ve 0-9 arasındaki rakamları içeren karakter topluluğu...rakamı yukarıda tanımlamıstım zaten rakam="0123456789" seklinde
sayac=0    # icerisindeki alfanümerik karakterlerin sayisini bulmak icin sayac tanımladım

for i in range(len(sifre)):
    for j in range(len(alfanümerik)):
        if(sifre[i]==alfanümerik[j]):    # sifrenin herhangi bir elemaninin alfanümerik karakter dizisi icindeki bir elemana esit olup olmadigini kontrol et
            sayac+=1       # esitse 1 artır


if(sayac==len(sifre)):     # eger hepsi esitse sayac,sifrenin uzunluguna esit olur.Biz olmamasını isteriz
    print("Şifre en az 1 tane alfanümerik olmayan karakter içermelidir.")

else:
    alfanümeriklik=1




# tekrarlayan karakter olup olmadigini kontrol et

tekrarlama=0   # --> bayrak 6

for i in range(len(sifre)-1):   # sifrenin uzunlugu-1 kadar git cunku indis 0 dan baslar
    if(sifre[i] == sifre[i+1]):    # sifenin i.elemaninin i+1. elemanina esit olup olmadigini kontrol et
        print("Şifre içinde tekrarlayan karakter bulunmamalıdır.")

tekrarlama=1


# kendi kriterimiz-1: şifre kullanıcı adı içeremez

kriter1=0  #-->bayrak 7

sayı=sifre.count(ad)  # count yardımı ile sifrenin içinde kaç tane ad olduğunu sayıyoruz
if(sayı>0):
    print("Şifre kullanıcı adı içeremez.")
else:
    kriter1=1



# kendi kriterimiz-2 :sifre sadece rakamlardan oluşamaz

kriter_2_sayac=0  # -->bayrak 8

kriter_2=0

for i in range(len(sifre)):
    for j in range(len(rakam)):
        if(sifre[i]==rakam[j]):
            kriter_2_sayac+=1


if(kriter_2_sayac==len(sifre)):
    print("Sifre sadece rakamlardan oluşamaz.")

else:
    kriter_2= 1



#En son doğru şifreyi seçip seçmediğimizi anlayacağız. Örnek şifre: F2tm3Erc?yas

if(uzunluk==1 and kbd==1 and rakamlık==1 and bosluk==1 and alfanümeriklik==1 and tekrarlama==1 and kriter1==1 and kriter_2==1):
    print("Şifreniz geçerlidir...")


# bu bölümde numaralandırdığım 8 tane bayrağımı kontrol ediyorum ve hepsi 1 e eşitse şifremi geçerli kılıyorum.
