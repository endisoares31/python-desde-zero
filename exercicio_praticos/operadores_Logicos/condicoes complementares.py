"""
Verificar se o carro é novo ou velho
Se o carro tiver pelo menos tres anos é novo
"""

idade = int(input("Digite a idade do seu carro: "))
if idade <= 3:
    print("O seu carro é novo")
else:
    print("Seu carro é velho")
