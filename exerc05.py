numero_limite=int(input("Escolha um número inteiro e positivo: "))
soma=0
for numero in range(1,numero_limite + 1):
    if numero %2==0:
        soma= soma + numero
print(f"A soma dos números pares 1 até {numero_limite} é: {soma}")
