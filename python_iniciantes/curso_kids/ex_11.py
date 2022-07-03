# Faca um programa que pergunte em que turno o usuário estuda.
# Peca para Digitar M-matutino, V-vespertino ou N-Noturno.
#Imprima a mensagem "Bom dia", "Boa tarde", "Boa Noite" ou valor inválido, conforme o caso.

print ('[M] = Matutino')
print ('[V] = Vespertino')
print ('[N] = Noturno')

turno = input ("Digite a letra que corresponde ao período que voce estuda: ").lower()

if turno == 'm':
	print('Bom dia')
elif turno == 'v':
	print('Boa tarde')
elif turno == 'n':
	print('Boa Noite')

else:
	print('Valor inválido')
