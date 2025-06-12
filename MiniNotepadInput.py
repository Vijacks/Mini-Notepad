import os
from venv import create

if not os.path.exists("Notlar.txt"):
    with open("Notlar.txt", "w"):
        pass

while True:
    ayar = input("Ayarı giriniz(ekle/sil/liste/çık): ")
    if ayar in ("ekle", "sil", "liste"):
        print("Yanlış komut girdiniz")
        continue
    elif ayar in ("çık"):
        break

    if ayar == "ekle":
        a = input("Notu Gir: ")
        with open("Notlar.txt", "a", encoding="utf-8") as f:

            f.write(a + "\n")
    elif ayar == "sil":
        a = input("Notu Gir: ")
        with open("Notlar.txt", "r", encoding="utf-8") as f:
            b = [x.strip() for x in f.readlines()]

        if a not in b:
            print(" Yazı bulunamadı ")
            exit(1)
        b.remove(a)
        with open("Notlar.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(b) + "\n")
    elif ayar == "liste":
        with open("Notlar.txt", "r", encoding="utf-8") as f:
            m = f.read().strip()
            if len(m) == 0:
                print("Bir notunuz bulunmamaktadır")
                continue
            m = m.split("\n")
            print("Notlarım(" + str(len(m)) + "):")
            for satır in m:
                print(satır.strip())
