idade = int(input("Digite sua idade: "))
if idade >= 18:
	if idade < 70:
		print("Voce pode receber o beneficio")
	else:
		print("Voce não pode receber o beneficio")
else: 
	print("Voce não pode receber o beneficio")
