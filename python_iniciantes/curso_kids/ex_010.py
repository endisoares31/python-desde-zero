vh = float(input ('Digite quanto voce ganha por hora: '))
ht = float (input ('Digite quantas horas voce trabalhou no mes '))
salario_bruto = vh * ht
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
total_desc = ir + inss + sindicato
salario_liq = salario_bruto - total_desc

print("voce pagou $ {:.2f} de imposto de renda".format(ir))
print("voce pagou $ {:.2f} ao INSS".format(inss))
print("Voce pagou $ {:.2f} ao sindicato".format(sindicato))
print ("Seu salário bruto é ${:.2f}".format(salario_bruto))
print ("Seu salario liquido é ${}".format(salario_liq))
