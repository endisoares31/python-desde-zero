 
  #Faca um programa para uma loja de tintas.
  #O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
  #Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e é vendida
  #e, latas de 18 litros, que custam R$80,00.
  
  #Informe ao usuário a quantidade de latas de tintas a serem comprados e o preco total.
  


area = int(input("Digite a área a ser pintada: "))

litros = area // 3

if area % 3 > 0:
	litros = litros + 1
	


latas = litros // 18
if litros % 18 > 0:
	latas = latas + 1

print ("Voce precisara de ", latas, "latas.")
print("Voce vai pagar R$", latas*80)
 
	
	

