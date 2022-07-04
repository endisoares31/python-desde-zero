#Faca um programa que peca um número e informe se o numero é inteiro ou decimal.

num = float(input('Digite um numero '))

if (num // 1 == num):
	print('Numero inteiro')
else:
	print('Numero decimal')
