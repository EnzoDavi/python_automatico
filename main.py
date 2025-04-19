import matplotlib.pyplot as plt
import trat
x = ["1","2", "3", "4", "5"]
y = [10,8, 6, 4, 2]

x = trat.tratamento(x)
plt.plot(x, y)
plt.savefig("grafico.png")