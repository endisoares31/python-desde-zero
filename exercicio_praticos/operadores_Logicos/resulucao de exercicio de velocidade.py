"""
Pergunte a velocidade de um carro, sopondo um valor inteiro. Caso ultrapasse 110 km/h, 
exiba uma mensagem dizendo que o usuário foi multado. Neste caso, exiba o valor da multa,
cobrando R$ 5,00 por km acima de 110

""" 
v = int(input("Velocidade: "))
if v > 110:
    print("Voce foi multado! ")
    multa = (v-110) * 5 
    print(f'Multa R$ {multa:.2f}')
else:
    print("Siga em frente, Boa Viagem!")