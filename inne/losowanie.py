import random

liczba = random.randint(1, 10)  # Losuje liczbę od 1 do 10
print(liczba)

liczba = random.uniform(1.5, 5.5)  # Losuje liczbę między 1.5 a 5.5
print(liczba)

kolory = ["czerwony", "zielony", "niebieski"]

losowy_kolor = random.choice(kolory)
print(losowy_kolor)

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9]

proba = random.sample(liczby, 3)  # Losuje 3 różne liczby
print(proba)
random.shuffle(liczby)  # Tasuje listę
print(liczby)