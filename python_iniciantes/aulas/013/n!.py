#Dado um numero inteiro nao negativo n, determinar n!

n = int(input("Digite n: "))

prod = 1
cont = 2

while cont <=5:
	prod = prod*cont
	cont = cont + 1 
print(n, "! =", prod)
