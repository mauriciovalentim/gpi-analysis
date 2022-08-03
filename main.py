from tkinter import *
from dataGetters import getPaises
from figBuild import tabelaDados

def chamarAux():
    tabelaDados(variable.get())

optionList = getPaises()
optionList.sort()

janela = Tk()
janela.title("GPI")
janela.iconbitmap("imgGPI.ico")
janela.resizable(False, False)
##janela.geometry("200x200")

variable = StringVar(janela)
variable.set(optionList[0])
menu = OptionMenu(janela, variable, *optionList)
menu.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Selecionar", command=chamarAux)
botao.grid(column=0, row=1, padx=10, pady=10)

info = Label(janela, text="Selecione um país para mostrar os dados")
info.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()