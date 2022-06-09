""""
Faca um programa que peca dois numeros, base e expoente, calcula e mostre o primeiro número elevado ao segundo número.
Não Ulitize a funcao potencia da Linguagem 
2**3 = 1*2*2*2*2 = 8
4**4 = 1*2*2*2*2 = 16
"""
# o Numero de expoente indica o numero de vezes que a base é multiplicada por ela mesma
#A potencia é o numero 1 multiplicado pela base o numero de expoente

base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

cont = 0 
produto = 1 
while cont < expoente:
    produto = produto*base
    cont = cont + 1 

print(base, "elevado a", expoente, "=", produto)