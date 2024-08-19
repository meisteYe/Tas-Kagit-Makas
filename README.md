# Taş, Kağıt, Makas - Emir Yusuf Ekelik

## Oyun Açıklaması

Bu oyun klasik taş, kağıt, makas oyununa bir yenilik getiriyor. Toplamda 6 farklı seçenekle oynanabilir ve oyun kuralları farklı puanlama sistemine dayalıdır. Kazanmak için stratejik düşünmeniz gerekecek!

## Kurallar

1. Oyun 2 galibiyet alan oyuncunun kazanmasıyla sona erer.
2. Taş ve kağıt ile kazanan 2 puan alır ve oyunu direkt kazanır.
3. Ateş ve toprak ile kazanan yarım puan alır.
4. Makas ve su ile kazanan 1 puan alır.
5. Beraberlik durumunda puan verilmez.
6. Oyun sonunda oyuncuya devam edip etmek istemediği sorulur. Oyundan çıkmak için 'exit' yazılabilir.

## Seçenekler ve Sonuçları

- **Taş:** Makası kırar, suyu engeller. (2 galibiyet puanı)
- **Kağıt:** Taşı kaplar, toprağı sarar. (2 galibiyet puanı)
- **Makas:** Kağıdı keser, toprağı kazar, su ile berabere kalır. (1 galibiyet puanı)
- **Ateş:** Kağıdı yakar, taşı ve makası eritir. (0.5 galibiyet puanı)
- **Su:** Ateşi söndürür, kağıdı ıslatır, makas ile berabere kalır. (1 galibiyet puanı)
- **Toprak:** Ateşi söndürür, suyu emer, taşı kaplar. (0.5 galibiyet puanı)

## Oyun Nasıl Oynanır

1. Oyun başladığında kullanıcı bir seçenek girer.
2. Bilgisayar rastgele bir seçim yapar.
3. Oyun kurallarına göre galibiyet veya beraberlik belirlenir.
4. 2 puana ulaşan oyuncu oyunu kazanır.

## Kullanım

Oyunu çalıştırmak için Python'u yüklemiş olmanız gerekmektedir. Oyunu başlatmak için aşağıdaki adımları izleyin:

```bash
git clone https://github.com/meisteYe/Tas-Kagit-Makas/
cd Tas-Kagit-Makas
python tkm_eye.py
