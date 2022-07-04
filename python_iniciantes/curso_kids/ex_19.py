#Escreva um programa que faca o computador 
#pensar aleartoriamente em um numero inteiro 
#entre 0 a 10 e peca ao usuário chutar qual foi o numero escolhido pelo computador

from random import randint

computador = randint(0,10)
jogador = int(input('Pensei em um número inteiro entre 0 e 10, tente advinhar...\n'))

if computador == jogador:
	print('Voce ganhou!')
else:
	print('Errou pensei no numero {}'.format(computador))


