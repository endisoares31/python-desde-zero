#Dizemos que um numero natural é triangular se ele é produto de tres numeros naturais consecutivos
# Exemplo: 120 é triangular, poius 4.5.6 ==120.
# Dado um inteiro nãonegativo n, verificar se n é triangular

num = int(input("Digite um numero: "))

i = 1

while i * (i + 1) * (i + 2) < num:
	i += 1

if i * (i + 1) * (i + 2) == num:
	print(num, "é triangular")
else:
	print(num, "não é triangular")
