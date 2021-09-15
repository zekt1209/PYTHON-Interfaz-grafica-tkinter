# -*- coding: utf-8 -*-
"""
Created on 14/09/2021

@author: VictorGuzman
"""

from tkinter import *
import re
abc = '0123456789abcdefghijklmnopqrstuvwxyz?¿,. '   # Definimos el abecedario para el cifrado

class aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('600x600')
        self.raiz.resizable(width=False, height=False)
        self.raiz.title('Expresiones regulares')
        label = Label(self.raiz, text="Validación de expresiones regulares")
        label.pack(side=TOP)

        self.textos = Frame(self.raiz)
        self.textos.pack(side=TOP)
        self.frameDeAbajo = Frame(self.raiz)
        self.frameDeAbajo.pack(side=BOTTOM)
        self.frameDeIzq = Frame(self.raiz)
        self.frameDeIzq.pack(side=LEFT)


        self.t1 = Entry(self.textos, width=40)
        self.t1.grid(row=0, column=0, padx=10, pady=10)
        self.t2 = Entry(self.textos, width=40)
        self.t2.grid(row=1, column=0)
        self.t3 = Entry(self.textos, width=40)
        self.t3.grid(row=2, column=0)
        self.t4 = Entry(self.textos, width=40)
        self.t4.grid(row=3, column=0)
        self.t5 = Entry(self.textos, width=30)
        self.t5.grid(row=5, column=1)
        self.t6 = Entry(self.textos, width=10)
        self.t6.grid(row=6, column=1)
        self.t7 = Entry(self.textos, width=30)
        self.t7.grid(row=9, column=1)
        self.t8 = Entry(self.textos, width=15)
        self.t8.grid(row=10, column=1)
        self.t9 = Entry(self.textos, width=30)
        self.t9.grid(row=7, column=1)
        self.t10 = Entry(self.textos, width=30)
        self.t10.grid(row=11, column=1)

        self.b1 = Button(self.textos, text='validar', command=lambda: self.validar(1))
        self.b1.grid(row=0, column=1, padx=10, pady=10)
        self.b2 = Button(self.textos, text='validar', command=lambda: self.validar(2))
        self.b2.grid(row=1, column=1, pady=10)
        self.b3 = Button(self.textos, text='validar', command=lambda: self.validar(3))
        self.b3.grid(row=2, column=1, pady=10)
        self.b4 = Button(self.textos, text='validar', command=lambda: self.validar(4))
        self.b4.grid(row=3, column=1, pady=10)
        self.b5 = Button(self.textos, text='cifrar', command=lambda: self.cifrar())
        self.b5.grid(row=6, column=2, pady=10)
        self.b6 = Button(self.textos, text='Descifrar', command=lambda: self.descifrar())
        self.b6.grid(row=10, column=2, pady=10)

        self.l1 = Label(self.textos, text='...')
        self.l1.grid(row=0, column=2)
        self.l2 = Label(self.textos, text='...')
        self.l2.grid(row=1, column=2)
        self.l3 = Label(self.textos, text='...')
        self.l3.grid(row=2, column=2)
        self.l4 = Label(self.textos, text='...')
        self.l4.grid(row=3, column=2)
        self.l5 = Label(self.textos, text='Cifrar mensaje')
        self.l5.grid(row=4, column=0, pady=15)
        self.l5.config(font="bold", background="green")
        self.l6 = Label(self.textos, text='Mensaje:')
        self.l6.grid(row=5, column=0)
        self.l7 = Label(self.textos, text='Clave:')
        self.l7.grid(row=6, column=0)
        self.l8 = Label(self.textos, text='Cadena cifrada: ')
        self.l8.grid(row=7, column=0)
        self.l10 = Label(self.textos, text='Descifrar mensaje')
        self.l10.grid(row=8, column=0, pady=15)
        self.l10.config(font="bold", background="green")
        self.l11 = Label(self.textos, text='Mensaje:')
        self.l11.grid(row=9, column=0)
        self.l12 = Label(self.textos, text='Clave')
        self.l12.grid(row=10, column=0)
        self.l13 = Label(self.textos, text='Cadena descifrada: ')
        self.l13.grid(row=11, column=0)

        self.bsalir = Button(self.frameDeAbajo, text="Salir", command=self.raiz.destroy)
        self.bsalir.pack(side=LEFT)
        self.blimpiar = Button(self.frameDeAbajo, text="Limpiar", command=self.limpiar)
        self.blimpiar.pack(side=LEFT)

        self.raiz.mainloop()

    def cifrar(self):  # Definimos la funcion cifrar y le mandamos esos 2 atributos

        cadena = self.t5.get().lower()  # Definimos nuestra cadena y la convertimos a minusculas
        clave = self.t6.get()  # Definimos el numero con el que vamos a cifrar
        #print(cifrar(cad, num))  # Imprime el resultado de la funcion cifrar


        text_cifrado = ''  # Creamos variable de texto vacia, donde se almacenara el texto ya cifrado
        for letra in cadena:  # Hacemos una iteracion en la variable cadena
            suma = abc.find(letra) + int(clave)  # Definimos suma como la posicion de la etra de abecedatio mas el numero clave
            modulo = int(suma) % len(abc)  # Definimos el modulo, convertimos suma a numero y se le aplica el modulo
            text_cifrado = text_cifrado + str(abc[modulo])  # Codificamos y aqui ya debe de estar la el texto recorrido

        self.t9.insert(0, text_cifrado)
        self.t9.config(fg="green")
        return text_cifrado


    def descifrar(self):

        cadena = self.t7.get().lower()  # Definimos nuestra cadena y la convertimos a minusculas
        clave = self.t8.get()  # Definimos el numero con el que vamos a descifrar

        text_cifrado = ''
        for letra in cadena:
            suma = abc.find(letra) - int(clave)
            modulo = int(suma) % len(abc)
            text_cifrado = text_cifrado + str(abc[modulo])

        self.t10.insert(0,text_cifrado)
        self.t10.config(fg="green")

        return text_cifrado


    def limpiar(self):
        self.t1.delete(first=0, last='end')
        self.t5.delete(first=0, last='end')
        self.t6.delete(first=0, last='end')
        self.t7.delete(first=0, last='end')
        self.t8.delete(first=0, last='end')

        self.l1.config(fg='black', text='...')
        self.t9.delete(0, len(self.t9.get()))
        self.t10.delete(0, len(self.t10.get()))


    def validar(self, numero):
        if (numero == 1):
            txtAValidar = self.t1.get()
            x = re.search("^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$", txtAValidar)
            if (x):
                self.l1.config(fg="green", text="IPv4 valida")
            else:
                self.l1.config(fg="red", text="IPv4 invalida")


app = aplicacion()