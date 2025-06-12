import os
import sys

argv = sys.argv[1:]

if len(argv) == 0 or argv[0] not in ("ekle", "çıkar", "liste"):
    print("Kullanım:")
    print("python MiniNotepad.py ekle <not>")
    print("python MiniNotepad.py çıkar <not>")
    print("python MiniNotepad.py liste")
    exit(1)

if not os.path.exists("Notlar.txt"):
    with open("Notlar.txt", "w"):
        pass

ayar = argv[0]
if ayar == "ekle":
    a = " ".join(argv[1:])
    with open("Notlar.txt", "a", encoding="utf-8") as f:
        f.write(a + "\n")
elif ayar == "çıkar":
    a = " ".join(argv[1:])
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
            exit(0)
        m = m.split("\n")
        print("Notlarım(" + str(len(m)) + "):")
        for satır in m:
            print(satır.strip())
