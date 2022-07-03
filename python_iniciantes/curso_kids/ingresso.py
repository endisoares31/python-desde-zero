idade = int(input("Digite a sua idade:  "))
ingresso = 50

if idade <= 18:
	ingresso = ingresso / 2
	
print("O valor do seu ingresso é R$ {}".format(ingresso))
