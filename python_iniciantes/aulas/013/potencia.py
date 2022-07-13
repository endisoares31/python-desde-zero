#Faca um programa que peca dois numeros, base e expoente, 
#calcula e mostre o primeiro numero elevado ao segundo numero.
#Nao utilize a funcao potencia da linguagem.

#O numero do expoente indica o numero de vezes que a base é multiplicada


base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

cont = 0
produto = 1
while cont < expoente:
	produto = produto*base
	cont = cont + 1
	
print(base, "elevado a", expoente, "=", produto)
	
