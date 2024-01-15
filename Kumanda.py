import random
import time

class Kumanda():

    def __init__(self,tv_durum = "Kapalı",tv_ses = 0,kanal_liste= ["Trt"],kanal= "Trt" ):

        self.tv_durum = tv_durum

        self.tv_ses = tv_ses

        self.kanal_liste = kanal_liste

        self.kanal = kanal


    def tv_ac(self):

        if (self.tv_durum == "Açık"):
            print("Televizyon zaten açık...")

        else:
            print("Televizyon açılıyor...")
            self.tv_durum = "Açık"


    def tv_kapat(self):

        if (self.tv_durum == "Kapalı"):
            print("Televizyon zaten kapalı...")

        else:
            print("Televizyon kapanıyor...")
            self.tv_durum = "Kapalı"


    def ses_ayarları(self):

        while True:
            cevap = input("Sesi Azalt: '<'\n, Sesi arttır: '>'\n, Çıkıs: çıkış ")

            if (cevap == "<"):
                if (self.tv_ses != 0):

                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)


            elif (cevap == ">"):
                if (self.tv_ses != 32):
                    self.tv_ses += 1
                    print("Ses:", self.tv_ses)

            else:
                print("Ses güncellendi:",self.tv_ses)
                break


    def kanal_ekle(self,kanal_ismi):

        print("kanal ekleniyor..")
        time.sleep(1)

        self.kanal_liste.append(kanal_ismi)

        print("Kanal eklendi...")


    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_liste)-1)

        self.kanal = self.kanal_liste[rastgele]

        print("Şuanki kanal:", self.kanal)


    def __len__(self):

        return len(self.kanal_liste)


    def __str__(self):

        return "Tv Durumu : {}\nTv Ses : {}\nKanal Liste: {}\nŞuanki Kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_liste,self.kanal)


kumanda = Kumanda()

print("""

Televizyon Uygulaması

1. Tv aç

2. Tv kapat

3. Ses ayarları

4. Kanal ekle

5. Kanal Sayısını öğrenme

6. Rastgele kanala geçme

7. Televizyon Bilgileri

Çıkmak için "q" ya basın.



""")


while True:

    işlem = input("işlem seçiniz.")

    if (işlem == "q"):
        print("Program sonlandırılıyor.")
        break

    elif(işlem == "1"):
        kumanda.tv_ac()

    elif(işlem == "2"):
        kumanda.tv_kapat()

    elif (işlem == "3"):
        kumanda.ses_ayarları()

    elif (işlem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak giriniz:")

        kanal_liste = kanal_isimleri.split(",")

        for eklenecekler in kanal_liste:
            kumanda.kanal_ekle(eklenecekler)

    elif (işlem == "5"):

        print("Kanal sayısı:",len(kumanda))

    elif (işlem == "6"):
        kumanda.rastgele_kanal()

    elif (işlem == "7"):
        print(kumanda)

    else:
        print("Geçersiz işlem.")
