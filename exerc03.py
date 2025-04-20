frase=input("Digite uma frase: ")
#imprimir frase original
print("Frase original: ", frase)
#frase com todas as letrs maiusculas
frase_maiuscula=frase.upper()
print("Frase com todas as letras maiusculas: ", frase_maiuscula)
#frase com letras minusculas
frase_minusculas= frase.lower()
print("Frase comm letras minusculas ", frase_minusculas)
# numero de caracteres na frases
frase_numeroscarac= len(frase)
print("Quantidade de caracteres na frase ", frase_numeroscarac)
#numeros de palavras na frase
frase_numerospalavras= frase.split()
print("Quantidades de palavras na frase ", frase_numerospalavras)
