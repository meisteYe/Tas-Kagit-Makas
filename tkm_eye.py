import random


def tas_kagit_makas_Emir_Yusuf_Ekelik():
    print("\nOyunuma Hoşgeldin. \nBu oyun bildiğin taş kağıt makas oyununa benzemiyor. \n6 seçeneğin var.\n"
          "\nAna hatlarıyla kurallarımız şunlardır:\n1: Üç sonuç var. Galibiyet, mağlubiyet veya beraberlik."
          "\n2: Skoru 2 olan kazanır."
          "\n3: Taş ve kağıt ile kazanan 2 puan alır ve oyunu direkt kazanır."
          "\n4. Ateş ve toprak ile kazanan yarım puan alır."
          "\n5. Beraberlikte puan eklenmez.\n"
          "\nSeçeneklerimiz şunlardır: Taş, Kağıt, Makas, Ateş, Su, Toprak\n"
          "\n \tTaş: Makası kırar. Suyu engeller."  # 2w 3l
          "\n \tKağıt: Taşı kaplar. Toprağı sarar."  # 2w 3l
          "\n \tMakas: Kağıdı keser. Toprağı kazar. Su ile berabere kalır."  # 2w 2l
          "\n \tAteş: Kağıdı yakar. Taşı ve makası eritir."  # 3w 2l
          "\n \tSu: Ateşi söndürür. Kağıdı ıslatır. Makas ile berabere kalır."  # 2w 2l
          "\n \tToprak: Ateşi söndürür. Suyu emer. Taşı kaplar.\n"  # 3w 2l 
          "\nHer oyun sonu oynamak isteyip istemediğiniz sorulacak.\nOyundan çıkmak için 'exit' yazabilirsin.\n")

    secenekler = ["taş", "kağıt", "makas", "ateş", "su", "toprak"]
    oyun_sayaci = 1
    tur_sayaci = 0
    oyuncu_galibiyet = 0
    bilgisayar_galibiyet = 0

    while True:
        print(f"Başlayalım :) Bol şans.\n")
        if oyuncu_galibiyet >= 2:
            print("Tebrikler, oyunu kazandınız!")
            break
        elif bilgisayar_galibiyet >= 2:
            print("Bilgisayar kazandı, çalış da gel:)")
            break

        while oyuncu_galibiyet < 2 and bilgisayar_galibiyet < 2:
            tur_sayaci += 1
            print(f"Oyun {oyun_sayaci}.\tTur {tur_sayaci} ")

            oyuncu_secimi = input("Lütfen bir seçenek giriniz. (Ateş, Su, Toprak, Taş, Kağıt veya Makas)\n").lower()

            if oyuncu_secimi == "exit":
                print("İlk elden gideceksen niye geldin kardeşim...")
                oyun_sayaci = 0
                break

            if oyuncu_secimi not in secenekler:
                tur_sayaci -= 1
                print("Geçersiz seçenek girdiniz. Lütfen tekrar deneyiniz.")
                continue

            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}\n")

            if oyuncu_secimi == bilgisayar_secimi:
                print("Berabere.")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi in ["makas", "su"] or
                  oyuncu_secimi == "kağıt" and bilgisayar_secimi in ["taş", "toprak"]):
                oyuncu_galibiyet += 2
                print(f"Oyuncu {oyuncu_galibiyet} puan ile oyunu kazandı!")
            elif (oyuncu_secimi == "ateş" and bilgisayar_secimi in ["kağıt", "taş", "makas"] or
                  oyuncu_secimi == "toprak" and bilgisayar_secimi in ["ateş", "su", "taş"]):
                oyuncu_galibiyet += 0.5
                print("Tebrikler turu kazandınız.")
            elif (oyuncu_secimi == "makas" and bilgisayar_secimi in ["kağıt", "toprak"] or
                  oyuncu_secimi == "su" and bilgisayar_secimi in ["ateş", "kağıt"]):
                oyuncu_galibiyet += 1
                print("Tebrikler turu kazandınız.")
            else:
                if (bilgisayar_secimi == "taş" and oyuncu_secimi in ["makas", "su"] or
                        bilgisayar_secimi == "kağıt" and oyuncu_secimi in ["taş", "toprak"]):
                    bilgisayar_galibiyet += 2
                    print(f"Bilgisayar {bilgisayar_galibiyet} puan ile oyunu kazandı!")
                elif (bilgisayar_secimi == "ateş" and oyuncu_secimi in ["kağıt", "taş", "makas"] or
                      bilgisayar_secimi == "toprak" and oyuncu_secimi in ["ateş", "su", "taş"]):
                    bilgisayar_galibiyet += 0.5
                    print("Turu bilgisayar kazandı.")
                elif (bilgisayar_secimi == "makas" and oyuncu_secimi in ["kağıt", "toprak"] or
                      bilgisayar_secimi == "su" and oyuncu_secimi in ["ateş", "kağıt"]):
                    bilgisayar_galibiyet += 1
                    print("Turu bilgisayar kazandı.")

            print(f"Oyuncu : {oyuncu_galibiyet} - {bilgisayar_galibiyet} : Bilgisayar\n")

        oyuncu_devam_et = input("Başka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
        bilgisayar_devam = random.choice(["evet", "hayır"])

        if oyuncu_devam_et == "hayır":
            print("Devam etmek istemiyorsunuz. Oyun sona erdi. Katıldığınız için teşekkür ederiz!")
            break
        else:
            if oyuncu_devam_et == "evet" and bilgisayar_devam == "evet":
                print("Oyun tekrardan başlıyor.")
                oyuncu_galibiyet = 0
                bilgisayar_galibiyet = 0
                oyun_sayaci += 1
                tur_sayaci = 0
            elif bilgisayar_devam == "hayır" and oyuncu_devam_et == "evet":
                print("Bilgisayar devam etmek istemiyor. Oyun sona erdi. Katıldığınız için teşekkür ederiz!")
                break
            else:
                print("Katıldığın için teşekkürler. Oyun sona erdi.")
                break


tas_kagit_makas_Emir_Yusuf_Ekelik()
