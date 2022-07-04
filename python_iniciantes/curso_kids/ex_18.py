#crie um programa que receba a idade de uma pessoa e 
#informe se é menor de idade (idade menor que 18 anos)
#maior de idade (idade maior que 18 anos) ou idoso (idade maior que 60 anos)

idade = int(input('Digite a sua idade: '))

if idade < 18:
	print ('Voce é menor de idade')
elif idade >= 18 and idade < 60:
	print ('Voce é maior de idade')
elif idade >= 60:
	print('Voce é idoso')
	
