numero = int(input("Digite um número  para saber a sua tabuada: "))
contador=1
while contador <= 10:
    resultado=numero * contador
    print(f"A tabuada de {numero} X {contador}={resultado}")
    contador += 1