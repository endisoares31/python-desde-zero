# O sistema de avalião é composto por tres provas. A primeira prova tem peso 2 a segunda prova tem peso 5
# A terceira tem peso 3. crie um programa que calcule a media de um aluno na disciplina.

nota1 = float(input ("Digite a primeira nota: "))
nota2 = float(input ("Digite a segunda nota: "))
nota3 = float(input ("Digite a terceita nota: "))

media = (nota1 * 2 + nota2 * 5 + nota3 * 3) / 10

print ( "A media do aluno é {}".format(media))
