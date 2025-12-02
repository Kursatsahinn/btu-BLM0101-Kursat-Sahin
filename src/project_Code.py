########################################## Birinci Aşama Başlangıcı ##################################################

#Birinci Aşama: Kullanıcıdan iki adet giriş değeri alarak mantık kapılarında bu iki değeri işleme tabi tutuyoruz

#Kullanıcı programı ilk çalıştırdığında ne yapacağını bilmediği için istediğimiz girdi şeklini kullanıcıya bir kereye mahsus söylüyoruz
print("Girdilerinizi 1 veya 0 şeklinde giriniz!")

#Doğru girdi yapılana kadar kullanıcıdan girdi isteyeceğimiz için sonsuz döngü oluşturarak bu işlemi gerçekleştiriyoruz
while True:
    #Kullanıcının girdiği birinci ve ikinci girdiyi input ile alarak int veri türüne çeviriyoruz
    birinci_girdi = int(input("Birinci Girdi Değeriniz: "))
    ikinci_girdi = int(input("İkinci Girdi Değeriniz: "))
    
    #Alınan girdiler istenilen şekilde ise döngüden çıkılarak bir sonraki yapılacak işleme geçiliyor
    if ((birinci_girdi == 1 or birinci_girdi == 0) and (ikinci_girdi == 1 or ikinci_girdi == 0)):
        break
    
    #Alınan girdiler istenilen şekilde değil ise bir uyarı mesajı göndererek döngünün başına dönülüyor
    else:
        print("İstenilen Şekilde Girdi Yapmalısınız!")

#Kullanıcıya kapı bilgilerinin verilmesi
print("1-AND Kapısı 2-OR Kapısı 3-XOR Kapısı 4-NAND Kapısı 5-NOT Kapısı")

#Kullanıcının işlem yapacağı kapıyı seçmek için bir input ile değer alınacaktır
islem = int(input("Girdilerinizi Hangi Kapıda İşleme Almak İstersiniz: "))

#Tekrarlı işlem yapılacağı için sonuç yazdırma işini bir fonksiyona atıyoruz
def sonuc_yazdirma(girdi_sonuc):
    print(f"Seçilen kapıdaki işlem sonucunuz: {girdi_sonuc}")


#İki girdinin işleme girmesi sonucu bir değer ortaya çıkacaktır bunu bir değişkene atayacağım ve adı girdi_sonuc olacaktır

#Alınan işleme göre match-case yapısı oluşturulması
#Burada 4 adet case bulunmakta bu yüzden hepsine tek tek print ile sonucu yazdırmaktansa daha önce hazırladığımız fonksiyon ile bu işlemi daha dinamik hala getiriyoruz

match islem:
    case 1:
        girdi_sonuc = birinci_girdi and ikinci_girdi
        sonuc_yazdirma(girdi_sonuc)
    case 2:
        girdi_sonuc = birinci_girdi or ikinci_girdi
        sonuc_yazdirma(girdi_sonuc)
    case 3:
        girdi_sonuc = int(birinci_girdi != ikinci_girdi) #Burada yapılan işlemler True veya False olarak döneceği için onları int değerine çeviriyoruz
        sonuc_yazdirma(girdi_sonuc)
    case 4:
        girdi_sonuc = int(not (birinci_girdi and ikinci_girdi)) #Burada yapılan işlemler True veya False olarak döneceği için onları int değerine çeviriyoruz
        sonuc_yazdirma(girdi_sonuc)
    case 5: #Bu case'de fonksiyon çağırmadık çünkü buradaki yazım bir kereye mahsustur.
        girdi_sonuc = int(not(birinci_girdi)) #Burada yapılan işlemler True veya False olarak döneceği için onları int değerine çeviriyoruz
        print(f"Girdiniz {birinci_girdi} NOT kapısından: {girdi_sonuc} olarak çıkar.") 
        
        girdi_sonuc2 = int(not(ikinci_girdi)) #Burada yapılan işlemler True veya False olarak döneceği için onları int değerine çeviriyoruz
        print(f"Girdiniz {ikinci_girdi} NOT kapısından: {girdi_sonuc2} olarak çıkar.")
    case _:
        print("İstenmeyen Seçim Yaptınız!")

########################################## Birinci Aşama Sonu ##################################################

########################################## İkinci Aşama Başlangıcı ##################################################

#İkinci Aşama: Üç değişkenli bir ifadenin  (A AND (B OR C)) tüm doğruluk tablosunu ekranda göstermek 

