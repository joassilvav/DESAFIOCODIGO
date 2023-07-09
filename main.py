import tkinter
import desafio1, desafio2, desafio4, desafio3, desafio5
from tkinter import *
import customtkinter as ctk
import requests

janela = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
janela.title('Desafio Pwc')
janela.geometry('600x300')
janela.resizable(width=False, height=False)
janela.iconbitmap('pwcS.ico')


def nova_tela(desafio):
    nova_janela = ctk.CTkToplevel()
    nova_janela.geometry('600x300')
    nova_janela.title('Desafio Pwc')
    nova_janela.transient(janela)
    nova_janela.focus_force()
    nova_janela.grab_set()
    nova_janela.resizable(width=False, height=False)
    ctk.CTkLabel(nova_janela, text='Digite uma frase desejada ou clique em teste de caso!', font=('Arial bold', 20)).pack(pady=20, padx=5)
    entr = ctk.CTkEntry(nova_janela, font=('Arial bold', 20))
    entr.pack(pady=20, padx=5)
    texto = StringVar()
    mdl = ctk.CTkLabel(nova_janela, textvariable=texto)
    mdl.pack()
    b1 =ctk.CTkButton(master=nova_janela, width=200, text='Analisar', command=lambda:boo(desafio, frase=entr.get(), nova_janela=nova_janela, texto=texto))
    b1.place(relx=0.12, rely=0.7, anchor=tkinter.W)
    b2 =ctk.CTkButton(master=nova_janela, width=200, text='Teste de caso', command=lambda:apag(desafio, frase=entr.get(), nova_janela=nova_janela, texto=texto, entr=entr))
    b2.place(relx=0.9, rely=0.7, anchor=tkinter.E)

def boo(escolha, frase, nova_janela, texto):
    match escolha:

        case 1:
            texto.set(desafio1.desafioum(frase))
        case 2:
            texto.set(desafio2.remov(frase))
        case 3:
            texto.set(desafio3.desafiotree(frase))
        case 4:
            texto.set(desafio4.desafiofour(frase))
        case 5:
            texto.set(desafio5.desafiofive(frase))


def apag(escolha, frase, nova_janela, texto, entr):
    match escolha:
        case 1:
            entr.delete(0, END)
            entr.insert(0, desafio1.getTestedeCaso())
            boo(escolha, desafio1.getTestedeCaso(), nova_janela, texto)
        case 2:
            entr.delete(0, END)
            entr.insert(0, desafio2.getTestedeCaso())
            boo(escolha, desafio2.getTestedeCaso(), nova_janela, texto)
        case 3:
            entr.delete(0, END)
            entr.insert(0, desafio3.getTestedeCaso())
            boo(escolha, desafio3.getTestedeCaso(), nova_janela, texto)

        case 4:
            entr.delete(0, END)
            entr.insert(0, desafio4.getTestedeCaso())
            boo(escolha, desafio4.getTestedeCaso(), nova_janela, texto)
        case 5:
            entr.delete(0, END)
            entr.insert(0, desafio5.getTestedeCaso())
            boo(escolha, desafio5.getTestedeCaso(), nova_janela, texto)



tex = ctk.CTkLabel(janela, text='Escolha um desafio!', font=('Arial bold', 20))
tex.pack(padx =5 ,pady=8)
d1 = ctk.CTkButton(master=janela, width=300, text='Desafio 1- manipulação de string', command=lambda:nova_tela(1))
d1.pack(padx =5 ,pady=8)
d2 = ctk.CTkButton(master=janela, width=300, text='Desafio 2- Removendo duplicados', command=lambda:nova_tela(2))
d2.pack(padx =5, pady=8)
d3 = ctk.CTkButton(master=janela, width=300, text='Desafio 3- Encontrar Substring palindroma', command=lambda:nova_tela(3))
d3.pack(padx =5, pady=8)
d4 = ctk.CTkButton(master=janela, width=300, text='Desafio 4- Colocar em letra maiúscula a primeira', command=lambda:nova_tela(4))
d4.pack(padx =5, pady=8)
d5 = ctk.CTkButton(master=janela, width=300, text='Desafio 5- Verificar se a string é um anagrama de um polímero', command=lambda:nova_tela(5))
d5.pack(padx =5, pady=8)


janela.mainloop()
