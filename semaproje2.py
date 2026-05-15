import sqlite3
import random

baglanti = sqlite3.connect("oyun.db")
imlec = baglanti.cursor()

imlec.execute("DROP TABLE IF EXISTS oyuncular")
imlec.execute("""
CREATE TABLE oyuncular (
    isim TEXT,
    rol TEXT,
    yasiyor INTEGER
)
""")
baglanti.commit()

print("=== Vampir-Köylü Oyunu Başlıyor ===")
oyuncu_listesi = []

while True:
    isim = input("Oyuncu ismi girin: ").strip()
    if not isim:
        print("İsim boş olamaz.")
        continue

    secim = input("Oyuncu girişi bitti mi? (e: evet, h: hayır): ").strip().lower()
    if secim == "e":
        oyuncu_listesi.append(isim)
        break
    elif secim == "h":
        oyuncu_listesi.append(isim)
        continue
    else:
        print("Hatalı seçim, lütfen sadece 'e' ya da 'h' girin.")
        continue

if len(oyuncu_listesi) < 6:
    print("Oyuncu sayısı yetersiz. En az 6 kişi olmalı.")
    exit()

roller = ["vampir", "doktor"] + ["köylü"] * (len(oyuncu_listesi) - 2)
karisik_roller = []
while roller:
    i = random.randint(0, len(roller) - 1)
    karisik_roller.append(roller[i])
    roller.pop(i)


for i in range(len(oyuncu_listesi)):
    imlec.execute("INSERT INTO oyuncular VALUES (?, ?, ?)", (oyuncu_listesi[i], karisik_roller[i], 1))
baglanti.commit()

print("\n--- ADMIN GİRİŞİ ---")
sifre = input("Rolleri görmek için admin şifresini girin: ")

if sifre == "admin123":
    print("\n--- ADMIN PANELİ: Roller Atandı ---")
    print("Sadece admin görebilir, oyunculara gösterme!\n")
    for satir in imlec.execute("SELECT isim, rol FROM oyuncular"):
        print(f"{satir[0]} → {satir[1]}")
    input("\nDevam etmek için ENTER tuşuna bas (admin ekranı kapanacak)...")
else:
    print("Hatalı şifre! Roller gösterilmeyecek.")

print("\nOyun başlıyor...\n")

def oyuncu_listesi_getir():
    oyuncular = []
    for satir in imlec.execute("SELECT isim FROM oyuncular WHERE yasiyor = 1"):
        oyuncular.append(satir[0])
    return oyuncular

def rol_getir(isim):
    for satir in imlec.execute("SELECT rol FROM oyuncular WHERE isim = ?", (isim,)):
        return satir[0]
    return None

def oyuncu_oldu(isim):
    imlec.execute("UPDATE oyuncular SET yasiyor = 0 WHERE isim = ?", (isim,))
    baglanti.commit()

def vampir_var_mi():
    for satir in imlec.execute("SELECT rol FROM oyuncular WHERE yasiyor = 1"):
        if satir[0] == "vampir":
            return True
    return False

while True:
    print("\n--- GECE OLDU ---")
    yasayanlar = oyuncu_listesi_getir()

    vampir_hedef = input("Vampir, hedef ismi gir (yasayanlar: {}): ".format(', '.join(yasayanlar))).strip()
    doktor_koruma = input("Doktor, koruyacağı ismi gir (yasayanlar: {}): ".format(', '.join(yasayanlar))).strip()

    if vampir_hedef == doktor_koruma:
        print(f"{vampir_hedef} korundu, kimse ölmedi.")
    elif vampir_hedef not in yasayanlar:
        print("Geçersiz hedef. Kimse ölmedi.")
    else:
        print(f"{vampir_hedef} gece öldü.")
        oyuncu_oldu(vampir_hedef)

    print("\n--- GÜNDÜZ OLDU ---")
    oylar = {}
    yasayanlar = oyuncu_listesi_getir()
    for o in yasayanlar:
        while True:
            oy = input(f"{o}, kimi vampir olarak oyluyorsun?: ").strip()
            if oy == o:
                print("Kendine oy veremezsin!")
                continue
            elif oy not in yasayanlar:
                print("Geçersiz isim.")
                continue
            else:
                oylar[oy] = oylar.get(oy, 0) + 1
                break

    if not oylar:
        print("Hiç oy kullanılmadı.")
    else:
        max_oy = max(oylar.values())
        en_cok_oy_alanlar = [isim for isim, oy in oylar.items() if oy == max_oy]

        if len(en_cok_oy_alanlar) > 1:
            print("Oylar eşit. Kimse ölmedi.")
        else:
            secilen = en_cok_oy_alanlar[0]
            print(f"{secilen} çoğunlukla öldü.")
            oyuncu_oldu(secilen)

            if rol_getir(secilen) == "vampir":
                print("Vampir öldü! Köylüler kazandı!")
                break
            else:
                print("Ama vampir değildi. Oyun devam ediyor...")

    if not vampir_var_mi():
        print("Vampir kalmadı. Köylüler kazandı!")
        break
