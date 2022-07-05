#Faca uma programa que pergunte ao usuário quantas pessoas serão sorteadas e pergunte o nome de caa uma delas.
#No fim do programa mostre a pessoa escolhida

import random
pessoas = []
qnt_pessoas = int(input('Quantas pessoas vão ser sorteadas:\n'))

for i in range(qnt_pessoas):
	selecionados = input('Qual o nome {} da pessoa: \n'.format(i+1))
	pessoas.append(selecionados)
	escolhido = random.choice(pessoas)
print ('A pessoa sorteada foi {}'.format(escolhido))
	
