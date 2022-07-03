#crie um programa que peca duas notas de prova de um aluno e calcule a sua media semestral

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = round((nota_1 + nota_2) / 2,1)

print ('A media do aluno é {}'.format(media))


