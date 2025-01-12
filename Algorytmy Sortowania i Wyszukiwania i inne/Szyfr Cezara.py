tekst= input("Wprowadz tekst: \n")
klucz = int(input("Wprowadz klucz: \n"))

wynik = ""
for i in range(len(tekst)):
    znak = ord(tekst[i])
    if(znak>= ord("a") and znak<= ord("z")) or (znak>=ord("A") and znak<=ord("Z")):
        if znak>= ord("a") and znak<=ord("z"):
            baza = ord("a")
        else:
            baza = ord("A")

        przesuniecie = (znak-baza+klucz) % 26
        nowyZnak = chr(baza+przesuniecie)
        wynik+=nowyZnak
    else:
        wynik+=tekst[i]
print(f"Wynik:\n{wynik}")