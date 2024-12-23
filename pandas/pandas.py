import pandas as pd
import numpy as np

# Tworzenie przykładowego DataFrame
np.random.seed(42)  # Dla powtarzalności wyników
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [24, 27, 22, 32, 29],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
    "Salary": [50000, 60000, 55000, 65000, 70000],
    "JoinDate": pd.date_range("2020-01-01", periods=5, freq="YE"),
    "Score": np.random.randint(50, 100, size=5),
}
df = pd.DataFrame(data)

# 1. Podstawowe informacje o danych
print("\nPodstawowe informacje:")
print(df.info())
print("\nStatystyki opisowe:")
print(df.describe())

# 2. Selekcja kolumn i wierszy
print("\nSelekcja jednej kolumny (Age):")
print(df["Age"])

print("\nSelekcja wierszy (pierwsze 3):")
print(df.head(3))

# 3. Filtrowanie danych
print("\nFiltr: osoby z pensją powyżej 60000:")
print(df[df["Salary"] > 60000])

# 4. Grupowanie i agregacja
print("\nŚrednia pensja w miastach:")
print(df.groupby("City")["Salary"].mean())

# 5. Dodawanie i modyfikacja kolumn
df["SalaryUSD"] = df["Salary"] * 1.1  # Dodanie nowej kolumny
df["IsSenior"] = df["Age"] > 30       # Kolumna logiczna
print("\nDataFrame po dodaniu kolumn:")
print(df)

# 6. Sortowanie danych
print("\nSortowanie po pensji rosnąco:")
print(df.sort_values(by="Salary"))

# 7. Obsługa brakujących danych
df.loc[2, "Salary"] = np.nan  # Symulowanie brakującej wartości
print("\nDataFrame z brakującymi danymi:")
print(df)

print("\nUzupełnianie brakujących danych:")
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df)

# 8. Przekształcanie danych (pivot)
print("\nPivot tabelka:")
print(df.pivot_table(values="Salary", index="City", columns="IsSenior", aggfunc="mean"))

# 9. Łączenie danych
data2 = {
    "Name": ["Alice", "Charlie", "Eva"],
    "Department": ["HR", "IT", "Finance"],
}
df2 = pd.DataFrame(data2)
print("\nŁączenie danych (merge):")
print(pd.merge(df, df2, on="Name", how="left"))

# 10. Eksport danych
df.to_csv("example_output.csv", index=False)
print("\nDataFrame zapisany do pliku 'example_output.csv'")

# 11. Wczytywanie danych
print("\nWczytywanie danych z pliku:")
loaded_df = pd.read_csv("example_output.csv")
print(loaded_df)

# 12. Wizualizacja danych (opcjonalnie z matplotlib/seaborn)
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x="City", y="Salary", data=df)
plt.title("Średnia pensja w miastach")
plt.show()
