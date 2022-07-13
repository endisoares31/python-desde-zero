a = int(input("Degite o primeiro numero: "))
b = int(input("Degite o segundo numero: "))
c = int(input("Degite o terceiro numero: "))


if a >= b >= c:
	print (a, b, c)
elif a >= c >= b:
	print (a, c, b)
elif b >= a >= c:
	print(b, a, c)
elif c >= a >= b:
	print (c, a, b)
else:
	print(c, b, a )
