import matplotlib.pyplot as plt
meses = ['Jan/22','Fev/22','Mar/22','Abr/22','Mai/22']
gasolina = [6.635, 6.600, 7.012, 7.245, 7.297]
diesel = [5.497, 5.592, 6.288, 6.602, 6.744]
etanol = [5.308, 4.744, 4.842, 5.326, 5.382]
plt.plot(meses, gasolina)
plt.plot(meses, diesel)
plt.plot(meses, etanol)
plt.scatter(meses, gasolina, label = "Gasolina")
plt.scatter(meses, diesel, label = "Diesel")
plt.scatter(meses, etanol, label = "Etanol")
plt.legend()
plt.xlabel("Meses")
plt.ylabel("Preços")
plt.title("Evolução dos Preços Médios dos Combustíveis em 2022")
plt.grid(True)
plt.show()