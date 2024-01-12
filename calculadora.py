#importando o tkinter:
from tkinter import *
from tkinter import ttk

#cores
cor1 = "#080808" #preto
cor2 = "#fcfcfc" #branco
cor3 = "#5274ab" #azul
cor4 = "#eceff1" #cinza
cor5 = "#ed8058" # LARANJA

janela = Tk()
janela.title("Calculadora")
janela.config(bg=cor1)
#tamanho da calculadora:
janela.geometry("235x310")
janela.resizable(width=False, height=False)
#criação de frames
frame_tela = Frame (janela, width=235, height=50, bg=cor3) 
frame_tela.grid(row=0, column=0)

frame_corpo= Frame (janela, width=235, height=268) 
frame_corpo.grid(row=1, column=0)

#variavel todos valores
todosValores = ""
#label
valor_text=StringVar()

#criação da função para entrada de valores 
def entradaV(event):
    global todosValores
    todosValores = todosValores + str(event)
    valor_text.set(todosValores)
  

#função para o calculo
def calcular ():
    global todosValores
    resultado = eval(todosValores)
    valor_text.set(str(resultado))

#limpar tela
def limparTela():
    global todosValores
    todosValores = ""
    valor_text.set("")

# criar um label ( aparecer o numero com o click)
app_label = Label(frame_tela, textvariable=valor_text, width=16, height=2, padx=7,relief=FLAT,anchor="e",justify=RIGHT,font=('Ivy 18 italic'),bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

#criação dos botoes 
# bg = background / fg = fonte(cor) / font = tipo da letra, tamanho e negrito / relief = modelo do quadrado em que a escrita ficara. 
botao1 = Button(frame_corpo,command = limparTela, text="C", width=18, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao1.place(x=-12, y =0)
botao3 = Button(frame_corpo, command= lambda: entradaV('/'),text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao3.place(x=177, y =0)

botao4 = Button(frame_corpo, command= lambda: entradaV('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao4.place(x=0, y =52)
botao4 = Button(frame_corpo, command= lambda: entradaV('8'),text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao4.place(x=59, y =52)
botao4 = Button(frame_corpo, command= lambda: entradaV('9'),text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao4.place(x=118, y =52)
botao5 = Button(frame_corpo, command= lambda: entradaV('*'),text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao5.place(x=177, y =52)


botao6 = Button(frame_corpo, command= lambda: entradaV('4'),text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao6.place(x=0, y =104)
botao7 = Button(frame_corpo, command= lambda: entradaV('5'),text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao7.place(x=59, y =104)
botao8 = Button(frame_corpo, command= lambda: entradaV('6'),text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao8.place(x=118, y =104)
botao9 = Button(frame_corpo, command= lambda: entradaV('-'),text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao9.place(x=177, y =104)

botao10 = Button(frame_corpo, command= lambda: entradaV('1'),text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao10.place(x=0, y =156)
botao11 = Button(frame_corpo, command= lambda: entradaV('2'),text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao11.place(x=59, y =156)
botao12= Button(frame_corpo, command= lambda: entradaV('3'),text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao12.place(x=118, y =156)
botao13= Button(frame_corpo, command= lambda: entradaV('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao13.place(x=177, y =156)


botao14 = Button(frame_corpo, command= lambda: entradaV('0'),text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao14.place(x=-1, y =208)
botao15 = Button(frame_corpo, command= lambda: entradaV('.'),text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao15.place(x=118, y =208)
botao16 = Button(frame_corpo, command= calcular,text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao16.place(x=177, y =208)



janela.mainloop()


