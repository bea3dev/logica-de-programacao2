numero = int(input("Digite um número: "))
total = 0
for a in range(1, numero + 1):
    if numero % a == 0:
        total += 1
if total == 2:
    print("Seu número é primo!")
else:
    print("Seu número não é primo!")
    