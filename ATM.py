import time as zaman


print("Bankamıza Hoşgeldiniz !, İşlem Yapmak İçin Kartınızı Sokunuz: ")
secim = input("Kartı sokmak için s, Bankamatikten ayrılamak için l yazınız.\n")
bakiye=500
if secim == "s":
    print("Kartınız okunuyor.")
    for i in range (3):
        print(".")
        zaman.sleep(3)
    sifre: int(input("Şifre: "))
    while True:
        secenek=int(input("""
        *******************
        1-HESABA PARA YÜKLE
        2-PARA ÇEKME 
        3-HESAP HAREKETLERİ
        4-ÇIKIŞ
        *******************
        """))
        while secenek <1 or secenek >4:
            secenek = int(input("Lütfen belirtilen aralıkta değer giriniz:"))
        if secenek == 1:
            yatırılanpara= int(input("Yatırılan miktarı giriniz: "))
            print("Paranız yatırılıyor.")
            for i in range(3):
                print(".")
                zaman.sleep(3)
            bakiye +=yatırılanpara
            print("Bakiye:",bakiye)
        elif secenek == 2:
            cekilenpara= int(input("Çekmek istediğiniz miktarı giriniz: "))
            if cekilenpara > bakiye:
                print("Bakiyeniz yetersizdir!")
            else :
                print("Paranız hazırlanıyor.")
                for i in range(3):
                    print(".")
                    zaman.sleep(3)
                bakiye -= cekilenpara
                print("Bakiye: ",bakiye)
        elif secenek == 3:
            print("""
            İsim : Hatice
            Soyisim: Ş****K
            IBAN:XXXXXXXXXXXX
            Bakiye: {}
            """ .format(bakiye))
        elif secenek == 4:
            break
