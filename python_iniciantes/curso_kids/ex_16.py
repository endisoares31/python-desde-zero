# faca um programa que leia tres números inteiros e mostre o maior e o menos deles.

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: ") )
num3 = int(input("Digite o terceiro numero: "))

maior = num1
menor = num1

if num2 > maior:
	maior = num2
if num3 > maior:
	maior = num3

if num2 < menor:
	menor = num2
if num3 < menor:
	menor = num3
	
print("O maior número digitado foi {} e o menor {}".format(maior,menor))
