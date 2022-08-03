from dataGetters import *
import matplotlib.pyplot as plt

def tabelaDados(pais):
    gpiAtual = getDataGPI2022()
    gpiPassado = getDataGPIPast()

    x = list()
    y = list()
    for key in gpiPassado[pais]:
        x.append(int(key))
        y.append(gpiPassado[pais][key])

    x.reverse()
    y.reverse()

    x.append(2022)
    y.append(gpiAtual[pais])
    plt.bar(x, y, label="dados do ano")
    plt.xlabel("Anos")
    plt.ylabel("Índice")
    #plt.xticks(x)
    plt.yticks([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
    plt.title(f"Global Peace Index - {pais}")
    plt.legend()
    plt.show()