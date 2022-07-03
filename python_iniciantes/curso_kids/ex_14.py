#Faca um programa que verifique se uma letra digitada é "F"ou "M". Dependendo s letra mostre na tela: 
#Femenino, Masculino, Sexo inválido

sexo = input('Digite [F]-Femenino ou [M]-Masculino: ').upper()

if sexo == "M":
	print("Sexo Masculino")
elif sexo == "F":
	print("Sexo Femenino")
else:
	print("Sexo Inválido") 
	
