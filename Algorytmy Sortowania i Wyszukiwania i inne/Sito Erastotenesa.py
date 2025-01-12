n = int(input("Do jakiej liczby szukamy liczb pierwszych? "))
liczbyPierwsze = [True] * (n + 1)

liczbyPierwsze[0] = False
liczbyPierwsze[1] = False

i = 2
while i * i <= n:
    if liczbyPierwsze[i]:
        j = i * i
        while j <= n:
            liczbyPierwsze[j] = False
            j += i
    i += 1

print("Liczby pierwsze to:")
for i in range(n + 1):
    if liczbyPierwsze[i]:
        print(i)
