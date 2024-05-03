import tkinter as tk
from tkinter import ttk
#janela

janela = tk.Tk()
janela.geometry('325x480')
janela.title('calculadora')

#criando frames
saida = tk.Frame(janela,width=325,height=120)
saida.grid(row=0,column=0)


entrada = tk.Frame(janela,width=325,height=360,bg='lightblue')
entrada.grid(row=1,column=0)

#saida label
#lista         
lista = []

label_saida = tk.Label(saida,text=lista,font=('arial',30))
label_saida.place(x=0,y=32)

#operação
def atualizar(botao):
    lista.append(botao)
    label_saida.configure(text=''.join(lista))


#resultado
def sinal_igual():
    try:
        resultado = eval(''.join(lista))    #transforma a string na operação
        label_saida.configure(text=resultado) #mostra no label_saida
    except:
        label_saida.configure(text='ERRO')
    finally:
        lista.clear()    #limpando a lista



def Clear():
    lista.clear()
    label_saida.configure(text='')

#criando botoes
# primeira linha 
bt_c = tk.Button(entrada,text='C',width=8,height=4,font=('arial 13'),relief='raised',overrelief='ridge',command=Clear)
bt_c.place(x=0,y=0)
bt_igual = tk.Button(entrada,text='=',width=8,height=4,font=('arial 13'),relief='raised',overrelief='ridge',command=sinal_igual)
bt_igual.place(x=81,y=0)

bt_soma = tk.Button(entrada,text='+',width=8,height=4,font=('arial 13'),relief='raised',overrelief='ridge',command=lambda:atualizar('+'))
bt_soma.place(x=162,y=0)

bt_menos = tk.Button(entrada,text='-',width=8,height=4,font=('arial 13'),relief='raised',overrelief='ridge',command=lambda:atualizar('-'))
bt_menos.place(x=243,y=0)

#segunda linha

bt_1 = tk.Button(entrada,text='1',width=8,height=4,font=('arial 13'),relief='raised',overrelief='ridge',command=lambda:atualizar('1'))
bt_1.place(x=0,y=90)

bt_2 = tk.Button(entrada,text='2',width=8,height=4,font=('arial 13'),relief='raised',overrelief='ridge',command=lambda:atualizar('2'))
bt_2.place(x=81,y=90)

bt_3 = tk.Button(entrada,text='3',width=8,height=4,font=('arial 13'),relief='raised',overrelief='ridge',command=lambda:atualizar('3'))
bt_3.place(x=162,y=90)

bt_mult = tk.Button(entrada,text='*',width=8,height=4,font=('arial 13'),relief='raised',overrelief='ridge',command=lambda:atualizar('*'))
bt_mult.place(x=243,y=90)

#terceira linha

bt_4 = tk.Button(entrada,text='4',width=8,height=4,font=('arial 13'),relief='raised',overrelief='ridge',command=lambda:atualizar('4'))
bt_4.place(x=0,y=180)

bt_5 = tk.Button(entrada,text='5',width=8,height=4,font=('arial 13'),relief='raised',overrelief='ridge',command=lambda:atualizar('5'))
bt_5.place(x=81,y=180)

bt_6 = tk.Button(entrada,text='6',width=8,height=4,font=('arial 13'),relief='raised',overrelief='ridge',command=lambda:atualizar('6'))
bt_6.place(x=162,y=180)

bt_divi = tk.Button(entrada,text='/',width=8,height=4,font=('arial 13'),relief='raised',overrelief='ridge',command=lambda:atualizar('/'))
bt_divi.place(x=243,y=180)

#quarta linha

bt_7 = tk.Button(entrada,text='7',width=8,height=4,font=('arial 13'),relief='raised',overrelief='ridge',command=lambda:atualizar('7'))
bt_7.place(x=0,y=270)

bt_8 = tk.Button(entrada,text='8',width=8,height=4,font=('arial 13'),relief='raised',overrelief='ridge',command=lambda:atualizar('8'))
bt_8.place(x=81,y=270)

bt_9 = tk.Button(entrada,text='9',width=8,height=4,font=('arial 13'),relief='raised',overrelief='ridge',command=lambda:atualizar('9'))
bt_9.place(x=162,y=270)

bt_0 = tk.Button(entrada,text='0',width=8,height=4,font=('arial 13'),relief='raised',overrelief='ridge',command=lambda:atualizar('0'))
bt_0.place(x=243,y=270)
janela.mainloop()




