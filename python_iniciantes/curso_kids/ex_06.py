# Faca um programa que leia o valor de um deposito e o valor da taxa de juros. 
# Calcula e exiba o valor do rendimento em um mes.

deposito = float(input("Digite o valor do seu deposito: "))

taxa = float(input("Digite o valor da taxa de juros: "))

rendimento = deposito * (taxa / 100) 

print ("O valor do rendimento mensal é de: {}".format(round(rendimento,2)))

