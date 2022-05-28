# -*- coding: utf-8 -*-
# encoding=utf8
TK_SILENCE_DEPRECATION=1
import sys

reload(sys)
sys.setdefaultencoding('utf8')


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from tkinter import *
import inventario

class Principal():

    def __init__(self):
        self.inventariodb=inventario.inventario()
        self.ventana1=tk.Tk()
        self.ventana1.title("Sistema de Captura de Datos")
        self.ventana1.geometry('550x500')
        self.ventana1.resizable(0,0)
        self.ventana1.configure(bg='white')
        button1 = ttk.Button(self.ventana1, text="Tenneco", command=self.maquila1)
        button1.place(x= 60, y= 300)
        button2 = ttk.Button(self.ventana1, text="Hopkins", command=self.maquila2)
        button2.place(x= 200, y= 300)
        button3 = ttk.Button(self.ventana1, text="AutoKabel", command=self.maquila3)
        button3.place(x= 340, y= 300)
        button4 = ttk.Button(self.ventana1, text="Trico", command=self.maquila4)
        button4.place(x= 130, y= 400)
        button5 = ttk.Button(self.ventana1, text="Vitessco", command=self.maquila5)
        button5.place(x= 270, y= 400)
        buttonSalir = ttk.Button(self.ventana1, text="Salir", command=quit)
        buttonSalir.place(x= 450, y= 450)
        
        img = tk.PhotoImage(file="dima2.gif")
        self.widget = Label(self.ventana1, image=img).place(x=110, y=40)
        
        
        self.ventana1.mainloop()
        
    
    def maquila1(self):
    
        self.maq1 = Toplevel()
        self.maq1.geometry('675x370')
        self.maq1.resizable(0,0)
        self.maq1.configure(bg='grey')
        self.cuaderno1 = ttk.Notebook(self.maq1)
        self.cuaderno1.grid(column=0, row=0, padx=0, pady=0)
        
        self.maq1.title("Tenneco")
        
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Captura")
        
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consultar")
        
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Modificar/Actualizar")
        
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Eliminar")
        
        #Menu Agregar
        
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="")
        self.labelframe1.grid(column=8, row=0, padx=5, pady=10)
        
        self.label0=ttk.Label(self.labelframe1, text="# Parte:")
        self.label0.grid(column=0, row=0, padx=4, pady=4)
        self.parte=tk.StringVar()
        self.entryparte=ttk.Entry(self.labelframe1, textvariable=self.parte)
        self.entryparte.grid(column=1, row=0, padx=4, pady=4)
        
        self.label1=ttk.Label(self.labelframe1, text="Ubicación:")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.ubi=tk.StringVar()
        self.entryubi=ttk.Entry(self.labelframe1, textvariable=self.ubi)
        self.entryubi.grid(column=1, row=1, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Cantidad:")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.cant=tk.StringVar()
        self.entrycant=ttk.Entry(self.labelframe1, textvariable=self.cant)
        self.entrycant.grid(column=1, row=2, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe1, text="Plano:")
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.plan=tk.StringVar()
        self.entryplan=ttk.Entry(self.labelframe1, textvariable=self.plan)
        self.entryplan.grid(column=1, row=3, padx=4, pady=4)
        
        self.label4=ttk.Label(self.labelframe1, text="Precio ($):")
        self.label4.grid(column=0, row=4, padx=4, pady=4)
        self.precio=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.precio)
        self.entryprecio.grid(column=1, row=4, padx=4, pady=4)
        
        self.label5=ttk.Label(self.labelframe1, text="Consumo:")
        self.label5.grid(column=0, row=5, padx=4, pady=4)
        self.con=tk.StringVar()
        self.entrycon=ttk.Entry(self.labelframe1, textvariable=self.con)
        self.entrycon.grid(column=1, row=5, padx=4, pady=4)
        
        self.buttonA = ttk.Button(self.labelframe1, text="Agregar", command=self.agregar1)
        self.buttonA.grid(column=4, row=9, padx=4, pady=4)
        
        self.buttonS = ttk.Button(self.labelframe1, text="Cerrar", command=self.maq1.destroy)
        self.buttonS.grid(column=5, row=9, padx=4, pady=4)
        
        #Menu Consultar
        
        self.labelframe1=ttk.LabelFrame(self.pagina2, text="")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.tree= ttk.Treeview(self.labelframe1, column=("column1", "column2", "column3", "column4", "column5", "column6", "column7"), show='headings')
        self.tree.grid(column=0, row=0, padx=5, pady=10)
        self.tree.heading("#1", text="Codigo", anchor=tk.S)
        self.tree.column("#1", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#2", text="# Parte", anchor=tk.S)
        self.tree.column("#2", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#3", text="Ubicación", anchor=tk.S)
        self.tree.column("#3", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#4", text="Cantidad", anchor=tk.S)
        self.tree.column("#4", width=120, minwidth=70, stretch=tk.NO)
        self.tree.heading("#5", text="Plano", anchor=tk.S)
        self.tree.column("#5", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#6", text="Precio", anchor=tk.S)
        self.tree.column("#6", width=120, minwidth=70, stretch=tk.NO)
        self.tree.heading("#7", text="Consumo", anchor=tk.S)
        self.tree.column("#7", width=70, minwidth=70, stretch=tk.NO)
        
        self.botonC=ttk.Button(self.labelframe1, text="Consultar", command=self.listar1)
        self.botonC.grid(column=0, row=2, padx=4, pady=4)
        
        #Menu Modificar
        
        self.labelframe1=ttk.LabelFrame(self.pagina3, text="")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigomod=tk.StringVar()
        self.entrycod=ttk.Entry(self.labelframe1, textvariable=self.codigomod)
        self.entrycod.grid(column=1, row=0, padx=4, pady=4)
        
        self.label11=ttk.Label(self.labelframe1, text="# Parte:")
        self.label11.grid(column=0, row=1, padx=4, pady=4)
        self.partemod=tk.StringVar()
        self.entryparte=ttk.Entry(self.labelframe1, textvariable=self.partemod)
        self.entryparte.grid(column=1, row=1, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Ubicación:")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.ubimod=tk.StringVar()
        self.entryubi=ttk.Entry(self.labelframe1, textvariable=self.ubimod)
        self.entryubi.grid(column=1, row=2, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe1, text="Cantidad:")
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.cantmod=tk.StringVar()
        self.entrycant=ttk.Entry(self.labelframe1, textvariable=self.cantmod)
        self.entrycant.grid(column=1, row=3, padx=4, pady=4)
        
        self.label4=ttk.Label(self.labelframe1, text="Plano:")
        self.label4.grid(column=0, row=4, padx=4, pady=4)
        self.planmod=tk.StringVar()
        self.entryplan=ttk.Entry(self.labelframe1, textvariable=self.planmod)
        self.entryplan.grid(column=1, row=4, padx=4, pady=4)
        
        self.label5=ttk.Label(self.labelframe1, text="Precio ($):")
        self.label5.grid(column=0, row=5, padx=4, pady=4)
        self.preciomod=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=5, padx=4, pady=4)
        
        self.label6=ttk.Label(self.labelframe1, text="Consumo:")
        self.label6.grid(column=0, row=6, padx=4, pady=4)
        self.conmod=tk.StringVar()
        self.entrycon=ttk.Entry(self.labelframe1, textvariable=self.conmod)
        self.entrycon.grid(column=1, row=6, padx=4, pady=4)
        
        self.botonSe=ttk.Button(self.labelframe1, text="Buscar", command=self.consultar_mod1)
        self.botonSe.grid(column=1, row=11, padx=4, pady=4)
       
        self.botonAc=ttk.Button(self.labelframe1, text="Actualizar", command=self.modifica1)
        self.botonAc.grid(column=2, row=11, padx=4, pady=4)
        
        #Menu Eliminar
        
        self.labelframe1=ttk.LabelFrame(self.pagina4, text="")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigoborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe1, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Eliminar", command=self.borrar1)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)
        
        
        # Respetar esta parte...
        
        self.maq1.transient(master=self.ventana1)
        self.maq1.grab_set()
        self.ventana1.wait_window(self.maq1)
   
    def maquila2(self):
    
        self.maq2 = Toplevel()
        self.maq2.geometry('675x370')
        self.maq2.resizable(0,0)
        self.maq2.configure(bg='grey')
        self.cuaderno1 = ttk.Notebook(self.maq2)
        self.cuaderno1.grid(column=0, row=0, padx=0, pady=0)
        
        self.maq2.title("Hopkins")
        
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Captura")
        
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consultar")
        
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Modificar")
        
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Eliminar")
        
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="")
        self.labelframe1.grid(column=8, row=0, padx=5, pady=10)
        
        self.label0=ttk.Label(self.labelframe1, text="# Parte:")
        self.label0.grid(column=0, row=0, padx=4, pady=4)
        self.parte=tk.StringVar()
        self.entryparte=ttk.Entry(self.labelframe1, textvariable=self.parte)
        self.entryparte.grid(column=1, row=0, padx=4, pady=4)
        
        self.label1=ttk.Label(self.labelframe1, text="Ubicación:")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.ubi=tk.StringVar()
        self.entryubi=ttk.Entry(self.labelframe1, textvariable=self.ubi)
        self.entryubi.grid(column=1, row=1, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Cantidad:")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.cant=tk.StringVar()
        self.entrycant=ttk.Entry(self.labelframe1, textvariable=self.cant)
        self.entrycant.grid(column=1, row=2, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe1, text="Plano:")
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.plan=tk.StringVar()
        self.entryplan=ttk.Entry(self.labelframe1, textvariable=self.plan)
        self.entryplan.grid(column=1, row=3, padx=4, pady=4)
        
        self.label4=ttk.Label(self.labelframe1, text="Precio ($):")
        self.label4.grid(column=0, row=4, padx=4, pady=4)
        self.precio=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.precio)
        self.entryprecio.grid(column=1, row=4, padx=4, pady=4)
        
        self.label5=ttk.Label(self.labelframe1, text="Consumo:")
        self.label5.grid(column=0, row=5, padx=4, pady=4)
        self.con=tk.StringVar()
        self.entrycon=ttk.Entry(self.labelframe1, textvariable=self.con)
        self.entrycon.grid(column=1, row=5, padx=4, pady=4)
        
        self.buttonA = ttk.Button(self.labelframe1, text="Agregar", command=self.agregar2)
        self.buttonA.grid(column=4, row=9, padx=4, pady=4)
        
        self.buttonS = ttk.Button(self.labelframe1, text="Cerrar", command=self.maq2.destroy)
        self.buttonS.grid(column=5, row=9, padx=4, pady=4)
        
        self.labelframe1=ttk.LabelFrame(self.pagina2, text="")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.tree= ttk.Treeview(self.labelframe1, column=("column1", "column2", "column3", "column4", "column5", "column6", "column7"), show='headings')
        self.tree.grid(column=0, row=0, padx=5, pady=10)
        self.tree.heading("#1", text="Codigo", anchor=tk.S)
        self.tree.column("#1", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#2", text="# Parte", anchor=tk.S)
        self.tree.column("#2", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#3", text="Ubicación", anchor=tk.S)
        self.tree.column("#3", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#4", text="Cantidad", anchor=tk.S)
        self.tree.column("#4", width=120, minwidth=70, stretch=tk.NO)
        self.tree.heading("#5", text="Plano", anchor=tk.S)
        self.tree.column("#5", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#6", text="Precio", anchor=tk.S)
        self.tree.column("#6", width=120, minwidth=70, stretch=tk.NO)
        self.tree.heading("#7", text="Consumo", anchor=tk.S)
        self.tree.column("#7", width=70, minwidth=70, stretch=tk.NO)
        
        self.botonC=ttk.Button(self.labelframe1, text="Consultar", command=self.listar2)
        self.botonC.grid(column=0, row=2, padx=4, pady=4)
        
        self.labelframe1=ttk.LabelFrame(self.pagina3, text="")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigomod=tk.StringVar()
        self.entrycod=ttk.Entry(self.labelframe1, textvariable=self.codigomod)
        self.entrycod.grid(column=1, row=0, padx=4, pady=4)
        
        self.label11=ttk.Label(self.labelframe1, text="# Parte:")
        self.label11.grid(column=0, row=1, padx=4, pady=4)
        self.partemod=tk.StringVar()
        self.entrynom=ttk.Entry(self.labelframe1, textvariable=self.partemod)
        self.entrynom.grid(column=1, row=1, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Ubicación:")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.ubimod=tk.StringVar()
        self.entryubi=ttk.Entry(self.labelframe1, textvariable=self.ubimod)
        self.entryubi.grid(column=1, row=2, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe1, text="Cantidad:")
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.cantmod=tk.StringVar()
        self.entrycant=ttk.Entry(self.labelframe1, textvariable=self.cantmod)
        self.entrycant.grid(column=1, row=3, padx=4, pady=4)
        
        self.label4=ttk.Label(self.labelframe1, text="Plano:")
        self.label4.grid(column=0, row=4, padx=4, pady=4)
        self.planmod=tk.StringVar()
        self.entryplan=ttk.Entry(self.labelframe1, textvariable=self.planmod)
        self.entryplan.grid(column=1, row=4, padx=4, pady=4)
        
        self.label5=ttk.Label(self.labelframe1, text="Precio ($):")
        self.label5.grid(column=0, row=5, padx=4, pady=4)
        self.preciomod=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=5, padx=4, pady=4)
        
        self.label6=ttk.Label(self.labelframe1, text="Consumo:")
        self.label6.grid(column=0, row=6, padx=4, pady=4)
        self.conmod=tk.StringVar()
        self.entrycon=ttk.Entry(self.labelframe1, textvariable=self.conmod)
        self.entrycon.grid(column=1, row=6, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe1, text="Buscar", command=self.consultar_mod2)
        self.boton1.grid(column=1, row=11, padx=4, pady=4)
       
        self.boton2=ttk.Button(self.labelframe1, text="Actualizar", command=self.modifica2)
        self.boton2.grid(column=2, row=11, padx=4, pady=4)
        
        self.labelframe1=ttk.LabelFrame(self.pagina4, text="")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        
        self.codigoborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe1, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Eliminar", command=self.borrar2)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)
        
        self.maq2.transient(master=self.ventana1)
        self.maq2.grab_set()
        self.ventana1.wait_window(self.maq2)
    
    def maquila3(self):
    
        self.maq3 = Toplevel()
        self.maq3.geometry('675x370')
        self.maq3.resizable(0,0)
        self.maq3.configure(bg='grey')
        self.cuaderno1 = ttk.Notebook(self.maq3)
        self.cuaderno1.grid(column=0, row=0, padx=0, pady=0)
        
        self.maq3.title("AutoKabel")
        
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Captura")
        
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consultar")
        
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Modificar")
        
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Eliminar")
        
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="")
        self.labelframe1.grid(column=8, row=0, padx=5, pady=10)
        
        self.label0=ttk.Label(self.labelframe1, text="# Parte:")
        self.label0.grid(column=0, row=0, padx=4, pady=4)
        self.parte=tk.StringVar()
        self.entryparte=ttk.Entry(self.labelframe1, textvariable=self.parte)
        self.entryparte.grid(column=1, row=0, padx=4, pady=4)
        
        self.label1=ttk.Label(self.labelframe1, text="Ubicación:")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.ubi=tk.StringVar()
        self.entryubi=ttk.Entry(self.labelframe1, textvariable=self.ubi)
        self.entryubi.grid(column=1, row=1, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Cantidad:")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.cant=tk.StringVar()
        self.entrycant=ttk.Entry(self.labelframe1, textvariable=self.cant)
        self.entrycant.grid(column=1, row=2, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe1, text="Plano:")
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.plan=tk.StringVar()
        self.entryplan=ttk.Entry(self.labelframe1, textvariable=self.plan)
        self.entryplan.grid(column=1, row=3, padx=4, pady=4)
        
        self.label4=ttk.Label(self.labelframe1, text="Precio ($):")
        self.label4.grid(column=0, row=4, padx=4, pady=4)
        self.precio=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.precio)
        self.entryprecio.grid(column=1, row=4, padx=4, pady=4)
        
        self.label5=ttk.Label(self.labelframe1, text="Consumo:")
        self.label5.grid(column=0, row=5, padx=4, pady=4)
        self.con=tk.StringVar()
        self.entrycon=ttk.Entry(self.labelframe1, textvariable=self.con)
        self.entrycon.grid(column=1, row=5, padx=4, pady=4)
        
        self.buttonA = ttk.Button(self.labelframe1, text="Agregar", command=self.agregar3)
        self.buttonA.grid(column=4, row=9, padx=4, pady=4)
        
        self.buttonS = ttk.Button(self.labelframe1, text="Cerrar", command=self.maq3.destroy)
        self.buttonS.grid(column=5, row=9, padx=4, pady=4)
        
        self.labelframe1=ttk.LabelFrame(self.pagina2, text="")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.tree= ttk.Treeview(self.labelframe1, column=("column1", "column2", "column3", "column4", "column5", "column6", "column7"), show='headings')
        self.tree.grid(column=0, row=0, padx=5, pady=10)
        self.tree.heading("#1", text="Codigo", anchor=tk.S)
        self.tree.column("#1", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#2", text="# Parte", anchor=tk.S)
        self.tree.column("#2", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#3", text="Ubicación", anchor=tk.S)
        self.tree.column("#3", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#4", text="Cantidad", anchor=tk.S)
        self.tree.column("#4", width=120, minwidth=70, stretch=tk.NO)
        self.tree.heading("#5", text="Plano", anchor=tk.S)
        self.tree.column("#5", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#6", text="Precio", anchor=tk.S)
        self.tree.column("#6", width=120, minwidth=70, stretch=tk.NO)
        self.tree.heading("#7", text="Consumo", anchor=tk.S)
        self.tree.column("#7", width=70, minwidth=70, stretch=tk.NO)
        
        self.botonC=ttk.Button(self.labelframe1, text="Consultar", command=self.listar3)
        self.botonC.grid(column=0, row=2, padx=4, pady=4)
        
        self.labelframe1=ttk.LabelFrame(self.pagina3, text="")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigomod=tk.StringVar()
        self.entrycod=ttk.Entry(self.labelframe1, textvariable=self.codigomod)
        self.entrycod.grid(column=1, row=0, padx=4, pady=4)
        
        self.label11=ttk.Label(self.labelframe1, text="# Parte:")
        self.label11.grid(column=0, row=1, padx=4, pady=4)
        self.partemod=tk.StringVar()
        self.entrynom=ttk.Entry(self.labelframe1, textvariable=self.partemod)
        self.entrynom.grid(column=1, row=1, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Ubicación:")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.ubimod=tk.StringVar()
        self.entryubi=ttk.Entry(self.labelframe1, textvariable=self.ubimod)
        self.entryubi.grid(column=1, row=2, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe1, text="Cantidad:")
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.cantmod=tk.StringVar()
        self.entrycant=ttk.Entry(self.labelframe1, textvariable=self.cantmod)
        self.entrycant.grid(column=1, row=3, padx=4, pady=4)
        
        self.label4=ttk.Label(self.labelframe1, text="Plano:")
        self.label4.grid(column=0, row=4, padx=4, pady=4)
        self.planmod=tk.StringVar()
        self.entryplan=ttk.Entry(self.labelframe1, textvariable=self.planmod)
        self.entryplan.grid(column=1, row=4, padx=4, pady=4)
        
        self.label5=ttk.Label(self.labelframe1, text="Precio ($):")
        self.label5.grid(column=0, row=5, padx=4, pady=4)
        self.preciomod=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=5, padx=4, pady=4)
        
        self.label6=ttk.Label(self.labelframe1, text="Consumo:")
        self.label6.grid(column=0, row=6, padx=4, pady=4)
        self.conmod=tk.StringVar()
        self.entrycon=ttk.Entry(self.labelframe1, textvariable=self.conmod)
        self.entrycon.grid(column=1, row=6, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe1, text="Buscar", command=self.consultar_mod3)
        self.boton1.grid(column=1, row=11, padx=4, pady=4)
       
        self.boton2=ttk.Button(self.labelframe1, text="Actualizar", command=self.modifica3)
        self.boton2.grid(column=2, row=11, padx=4, pady=4)
        
        self.labelframe1=ttk.LabelFrame(self.pagina4, text="")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        
        self.codigoborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe1, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Eliminar", command=self.borrar3)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)
        
        self.maq3.transient(master=self.ventana1)
        self.maq3.grab_set()
        self.ventana1.wait_window(self.maq3)
    
    def maquila4(self):
    
        self.maq4 = Toplevel()
        self.maq4.geometry('675x370')
        self.maq4.resizable(0,0)
        self.maq4.configure(bg='grey')
        self.cuaderno1 = ttk.Notebook(self.maq4)
        self.cuaderno1.grid(column=0, row=0, padx=0, pady=0)
        
        self.maq4.title("Trico")
        
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Captura")
        
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consultar")
        
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Modificar")
        
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Eliminar")
        
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="")
        self.labelframe1.grid(column=8, row=0, padx=5, pady=10)
        
        self.label0=ttk.Label(self.labelframe1, text="# Parte:")
        self.label0.grid(column=0, row=0, padx=4, pady=4)
        self.parte=tk.StringVar()
        self.entryparte=ttk.Entry(self.labelframe1, textvariable=self.parte)
        self.entryparte.grid(column=1, row=0, padx=4, pady=4)
        
        self.label1=ttk.Label(self.labelframe1, text="Ubicación:")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.ubi=tk.StringVar()
        self.entryubi=ttk.Entry(self.labelframe1, textvariable=self.ubi)
        self.entryubi.grid(column=1, row=1, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Cantidad:")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.cant=tk.StringVar()
        self.entrycant=ttk.Entry(self.labelframe1, textvariable=self.cant)
        self.entrycant.grid(column=1, row=2, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe1, text="Plano:")
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.plan=tk.StringVar()
        self.entryplan=ttk.Entry(self.labelframe1, textvariable=self.plan)
        self.entryplan.grid(column=1, row=3, padx=4, pady=4)
        
        self.label4=ttk.Label(self.labelframe1, text="Precio ($):")
        self.label4.grid(column=0, row=4, padx=4, pady=4)
        self.precio=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.precio)
        self.entryprecio.grid(column=1, row=4, padx=4, pady=4)
        
        self.label5=ttk.Label(self.labelframe1, text="Consumo:")
        self.label5.grid(column=0, row=5, padx=4, pady=4)
        self.con=tk.StringVar()
        self.entrycon=ttk.Entry(self.labelframe1, textvariable=self.con)
        self.entrycon.grid(column=1, row=5, padx=4, pady=4)
        
        self.buttonA = ttk.Button(self.labelframe1, text="Agregar", command=self.agregar4)
        self.buttonA.grid(column=4, row=9, padx=4, pady=4)
        
        self.buttonS = ttk.Button(self.labelframe1, text="Cerrar", command=self.maq4.destroy)
        self.buttonS.grid(column=5, row=9, padx=4, pady=4)
        
        self.labelframe1=ttk.LabelFrame(self.pagina2, text="")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.tree= ttk.Treeview(self.labelframe1, column=("column1", "column2", "column3", "column4", "column5", "column6", "column7"), show='headings')
        self.tree.grid(column=0, row=0, padx=5, pady=10)
        self.tree.heading("#1", text="Codigo", anchor=tk.S)
        self.tree.column("#1", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#2", text="# Parte", anchor=tk.S)
        self.tree.column("#2", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#3", text="Ubicación", anchor=tk.S)
        self.tree.column("#3", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#4", text="Cantidad", anchor=tk.S)
        self.tree.column("#4", width=120, minwidth=70, stretch=tk.NO)
        self.tree.heading("#5", text="Plano", anchor=tk.S)
        self.tree.column("#5", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#6", text="Precio", anchor=tk.S)
        self.tree.column("#6", width=120, minwidth=70, stretch=tk.NO)
        self.tree.heading("#7", text="Consumo", anchor=tk.S)
        self.tree.column("#7", width=70, minwidth=70, stretch=tk.NO)
        
        self.botonC=ttk.Button(self.labelframe1, text="Consultar", command=self.listar4)
        self.botonC.grid(column=0, row=2, padx=4, pady=4)
        
        self.labelframe1=ttk.LabelFrame(self.pagina3, text="")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigomod=tk.StringVar()
        self.entrycod=ttk.Entry(self.labelframe1, textvariable=self.codigomod)
        self.entrycod.grid(column=1, row=0, padx=4, pady=4)
        
        self.label11=ttk.Label(self.labelframe1, text="# Parte:")
        self.label11.grid(column=0, row=1, padx=4, pady=4)
        self.partemod=tk.StringVar()
        self.entrynom=ttk.Entry(self.labelframe1, textvariable=self.partemod)
        self.entrynom.grid(column=1, row=1, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Ubicación:")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.ubimod=tk.StringVar()
        self.entryubi=ttk.Entry(self.labelframe1, textvariable=self.ubimod)
        self.entryubi.grid(column=1, row=2, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe1, text="Cantidad:")
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.cantmod=tk.StringVar()
        self.entrycant=ttk.Entry(self.labelframe1, textvariable=self.cantmod)
        self.entrycant.grid(column=1, row=3, padx=4, pady=4)
        
        self.label4=ttk.Label(self.labelframe1, text="Plano:")
        self.label4.grid(column=0, row=4, padx=4, pady=4)
        self.planmod=tk.StringVar()
        self.entryplan=ttk.Entry(self.labelframe1, textvariable=self.planmod)
        self.entryplan.grid(column=1, row=4, padx=4, pady=4)
        
        self.label5=ttk.Label(self.labelframe1, text="Precio ($):")
        self.label5.grid(column=0, row=5, padx=4, pady=4)
        self.preciomod=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=5, padx=4, pady=4)
        
        self.label6=ttk.Label(self.labelframe1, text="Consumo:")
        self.label6.grid(column=0, row=6, padx=4, pady=4)
        self.conmod=tk.StringVar()
        self.entrycon=ttk.Entry(self.labelframe1, textvariable=self.conmod)
        self.entrycon.grid(column=1, row=6, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe1, text="Buscar", command=self.consultar_mod4)
        self.boton1.grid(column=1, row=11, padx=4, pady=4)
       
        self.boton2=ttk.Button(self.labelframe1, text="Actualizar", command=self.modifica4)
        self.boton2.grid(column=2, row=11, padx=4, pady=4)
        
        self.labelframe1=ttk.LabelFrame(self.pagina4, text="")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        
        self.codigoborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe1, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Eliminar", command=self.borrar4)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)
        
        
        self.maq4.transient(master=self.ventana1)
        self.maq4.grab_set()
        self.ventana1.wait_window(self.maq4)
    
    def maquila5(self):
    
        self.maq5 = Toplevel()
        self.maq5.geometry('675x370')
        self.maq5.resizable(0,0)
        self.maq5.configure(bg='grey')
        self.cuaderno1 = ttk.Notebook(self.maq5)
        self.cuaderno1.grid(column=0, row=0, padx=0, pady=0)
        
        self.maq5.title("Trico")
        
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Captura")
        
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consultar")
        
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Modificar")
        
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Eliminar")
        
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="")
        self.labelframe1.grid(column=8, row=0, padx=5, pady=10)
        
        self.label0=ttk.Label(self.labelframe1, text="# Parte:")
        self.label0.grid(column=0, row=0, padx=4, pady=4)
        self.parte=tk.StringVar()
        self.entryparte=ttk.Entry(self.labelframe1, textvariable=self.parte)
        self.entryparte.grid(column=1, row=0, padx=4, pady=4)
        
        self.label1=ttk.Label(self.labelframe1, text="Ubicación:")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.ubi=tk.StringVar()
        self.entryubi=ttk.Entry(self.labelframe1, textvariable=self.ubi)
        self.entryubi.grid(column=1, row=1, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Cantidad:")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.cant=tk.StringVar()
        self.entrycant=ttk.Entry(self.labelframe1, textvariable=self.cant)
        self.entrycant.grid(column=1, row=2, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe1, text="Plano:")
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.plan=tk.StringVar()
        self.entryplan=ttk.Entry(self.labelframe1, textvariable=self.plan)
        self.entryplan.grid(column=1, row=3, padx=4, pady=4)
        
        self.label4=ttk.Label(self.labelframe1, text="Precio ($):")
        self.label4.grid(column=0, row=4, padx=4, pady=4)
        self.precio=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.precio)
        self.entryprecio.grid(column=1, row=4, padx=4, pady=4)
        
        self.label5=ttk.Label(self.labelframe1, text="Consumo:")
        self.label5.grid(column=0, row=5, padx=4, pady=4)
        self.con=tk.StringVar()
        self.entrycon=ttk.Entry(self.labelframe1, textvariable=self.con)
        self.entrycon.grid(column=1, row=5, padx=4, pady=4)
        
        self.buttonA = ttk.Button(self.labelframe1, text="Agregar", command=self.agregar5)
        self.buttonA.grid(column=4, row=9, padx=4, pady=4)
        
        self.buttonS = ttk.Button(self.labelframe1, text="Cerrar", command=self.maq5.destroy)
        self.buttonS.grid(column=5, row=9, padx=4, pady=4)
        
        self.labelframe1=ttk.LabelFrame(self.pagina2, text="")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.tree= ttk.Treeview(self.labelframe1, column=("column1", "column2", "column3", "column4", "column5", "column6", "column7"), show='headings')
        self.tree.grid(column=0, row=0, padx=5, pady=10)
        self.tree.heading("#1", text="Codigo", anchor=tk.S)
        self.tree.column("#1", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#2", text="# Parte", anchor=tk.S)
        self.tree.column("#2", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#3", text="Ubicación", anchor=tk.S)
        self.tree.column("#3", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#4", text="Cantidad", anchor=tk.S)
        self.tree.column("#4", width=120, minwidth=70, stretch=tk.NO)
        self.tree.heading("#5", text="Plano", anchor=tk.S)
        self.tree.column("#5", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#6", text="Precio", anchor=tk.S)
        self.tree.column("#6", width=120, minwidth=70, stretch=tk.NO)
        self.tree.heading("#7", text="Consumo", anchor=tk.S)
        self.tree.column("#7", width=70, minwidth=70, stretch=tk.NO)
        
        self.botonC=ttk.Button(self.labelframe1, text="Consultar", command=self.listar5)
        self.botonC.grid(column=0, row=2, padx=4, pady=4)
        
        self.labelframe1=ttk.LabelFrame(self.pagina3, text="")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigomod=tk.StringVar()
        self.entrycod=ttk.Entry(self.labelframe1, textvariable=self.codigomod)
        self.entrycod.grid(column=1, row=0, padx=4, pady=4)
        
        self.label11=ttk.Label(self.labelframe1, text="# Parte:")
        self.label11.grid(column=0, row=1, padx=4, pady=4)
        self.partemod=tk.StringVar()
        self.entrynom=ttk.Entry(self.labelframe1, textvariable=self.partemod)
        self.entrynom.grid(column=1, row=1, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Ubicación:")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.ubimod=tk.StringVar()
        self.entryubi=ttk.Entry(self.labelframe1, textvariable=self.ubimod)
        self.entryubi.grid(column=1, row=2, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe1, text="Cantidad:")
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.cantmod=tk.StringVar()
        self.entrycant=ttk.Entry(self.labelframe1, textvariable=self.cantmod)
        self.entrycant.grid(column=1, row=3, padx=4, pady=4)
        
        self.label4=ttk.Label(self.labelframe1, text="Plano:")
        self.label4.grid(column=0, row=4, padx=4, pady=4)
        self.planmod=tk.StringVar()
        self.entryplan=ttk.Entry(self.labelframe1, textvariable=self.planmod)
        self.entryplan.grid(column=1, row=4, padx=4, pady=4)
        
        self.label5=ttk.Label(self.labelframe1, text="Precio ($):")
        self.label5.grid(column=0, row=5, padx=4, pady=4)
        self.preciomod=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=5, padx=4, pady=4)
        
        self.label6=ttk.Label(self.labelframe1, text="Consumo:")
        self.label6.grid(column=0, row=6, padx=4, pady=4)
        self.conmod=tk.StringVar()
        self.entrycon=ttk.Entry(self.labelframe1, textvariable=self.conmod)
        self.entrycon.grid(column=1, row=6, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe1, text="Buscar", command=self.consultar_mod5)
        self.boton1.grid(column=1, row=11, padx=4, pady=4)
       
        self.boton2=ttk.Button(self.labelframe1, text="Actualizar", command=self.modifica5)
        self.boton2.grid(column=2, row=11, padx=4, pady=4)
        
        self.labelframe1=ttk.LabelFrame(self.pagina4, text="")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        
        self.codigoborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe1, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Eliminar", command=self.borrar5)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)
        
        
        self.maq5.transient(master=self.ventana1)
        self.maq5.grab_set()
        self.ventana1.wait_window(self.maq5)
    
    
    def agregar1(self):
        datos=(self.parte.get(), self.ubi.get(), self.cant.get(), self.plan.get(), self.precio.get(), self.con.get())
        self.inventariodb.alta1(datos)
        mb.showinfo("Información", "Los datos de Tenneco fueron agregados correctamente")
        self.parte.set("")
        self.ubi.set("")
        self.cant.set("")
        self.plan.set("")
        self.precio.set("")
        self.con.set("")
        
    def agregar2(self):
        datos=(self.parte.get(), self.ubi.get(), self.cant.get(), self.plan.get(), self.precio.get(), self.con.get())
        self.inventariodb.alta2(datos)
        mb.showinfo("Información", "Los datos Hopkins fueron agregados correctamente")
        self.parte.set("")
        self.ubi.set("")
        self.cant.set("")
        self.plan.set("")
        self.precio.set("")
        self.con.set("")
    
    def agregar3(self):
        datos=(self.parte.get(), self.ubi.get(), self.cant.get(), self.plan.get(), self.precio.get(), self.con.get())
        self.inventariodb.alta3(datos)
        mb.showinfo("Información", "Los datos de AutoKabel fueron agregados correctamente")
        self.parte.set("")
        self.ubi.set("")
        self.cant.set("")
        self.plan.set("")
        self.precio.set("")
        self.con.set("")
        
    def agregar4(self):
        datos=(self.parte.get(), self.ubi.get(), self.cant.get(), self.plan.get(), self.precio.get(), self.con.get())
        self.inventariodb.alta4(datos)
        mb.showinfo("Información", "Los datos de Trico fueron agregados correctamente")
        self.parte.set("")
        self.ubi.set("")
        self.cant.set("")
        self.plan.set("")
        self.precio.set("")
        self.con.set("")
        
    def agregar5(self):
        datos=(self.parte.get(), self.ubi.get(), self.cant.get(), self.plan.get(), self.precio.get(), self.con.get())
        self.inventariodb.alta5(datos)
        mb.showinfo("Información", "Los datos de Vitessco fueron agregados correctamente")
        self.parte.set("")
        self.ubi.set("")
        self.cant.set("")
        self.plan.set("")
        self.precio.set("")
        self.con.set("")
        
    def listar1(self):
        respuesta=self.inventariodb.view1()
        self.tree.delete(*self.tree.get_children())
        for row in respuesta:
            self.tree.insert("", tk.END, values=row)

    def listar2(self):
        respuesta=self.inventariodb.view2()
        self.tree.delete(*self.tree.get_children())
        for row in respuesta:
            self.tree.insert("", tk.END, values=row)
            
    def listar3(self):
        respuesta=self.inventariodb.view3()
        self.tree.delete(*self.tree.get_children())
        for row in respuesta:
            self.tree.insert("", tk.END, values=row)
            
    def listar4(self):
        respuesta=self.inventariodb.view4()
        self.tree.delete(*self.tree.get_children())
        for row in respuesta:
            self.tree.insert("", tk.END, values=row)

    def listar5(self):
        respuesta=self.inventariodb.view5()
        self.tree.delete(*self.tree.get_children())
        for row in respuesta:
            self.tree.insert("", tk.END, values=row)
            
    def consultar_mod1(self):
        datos=(self.codigomod.get())
        respuesta=self.inventariodb.consulta1(datos)
        if len(respuesta)>0:
            self.partemod.set(respuesta[0][0])
            self.ubimod.set(respuesta[0][1])
            self.cantmod.set(respuesta[0][2])
            self.planmod.set(respuesta[0][3])
            self.preciomod.set(respuesta[0][4])
            self.conmod.set(respuesta[0][5])
        else:
            self.codigomod.set('')
            self.partemod.set('')
            self.ubimod.set('')
            self.cantmod.set('')
            self.planmod.set('')
            self.preciomod.set('')
            self.conmod.set('')
            mb.showinfo("Información", "No existe dato con dicho código")
            
    def consultar_mod2(self):
        datos=(self.codigomod.get())
        respuesta=self.inventariodb.consulta2(datos)
        if len(respuesta)>0:
            self.partemod.set(respuesta[0][0])
            self.ubimod.set(respuesta[0][1])
            self.cantmod.set(respuesta[0][2])
            self.planmod.set(respuesta[0][3])
            self.preciomod.set(respuesta[0][4])
            self.conmod.set(respuesta[0][5])
        else:
            self.codigomod.set('')
            self.partemod.set('')
            self.ubimod.set('')
            self.cantmod.set('')
            self.planmod.set('')
            self.preciomod.set('')
            self.conmod.set('')
            mb.showinfo("Información", "No existe dato con dicho código")
    
    def consultar_mod3(self):
        datos=(self.codigomod.get())
        respuesta=self.inventariodb.consulta3(datos)
        if len(respuesta)>0:
            self.partemod.set(respuesta[0][0])
            self.ubimod.set(respuesta[0][1])
            self.cantmod.set(respuesta[0][2])
            self.planmod.set(respuesta[0][3])
            self.preciomod.set(respuesta[0][4])
            self.conmod.set(respuesta[0][5])
        else:
            self.codigomod.set('')
            self.partemod.set('')
            self.ubimod.set('')
            self.cantmod.set('')
            self.planmod.set('')
            self.preciomod.set('')
            self.conmod.set('')
            mb.showinfo("Información", "No existe dato con dicho código")
            
    def consultar_mod4(self):
        datos=(self.codigomod.get())
        respuesta=self.inventariodb.consulta4(datos)
        if len(respuesta)>0:
            self.partemod.set(respuesta[0][0])
            self.ubimod.set(respuesta[0][1])
            self.cantmod.set(respuesta[0][2])
            self.planmod.set(respuesta[0][3])
            self.preciomod.set(respuesta[0][4])
            self.conmod.set(respuesta[0][5])
        else:
            self.codigomod.set('')
            self.partemod.set('')
            self.ubimod.set('')
            self.cantmod.set('')
            self.planmod.set('')
            self.preciomod.set('')
            self.conmod.set('')
            mb.showinfo("Información", "No existe dato con dicho código")
            
    def consultar_mod5(self):
        datos=(self.codigomod.get())
        respuesta=self.inventariodb.consulta5(datos)
        if len(respuesta)>0:
            self.partemod.set(respuesta[0][0])
            self.ubimod.set(respuesta[0][1])
            self.cantmod.set(respuesta[0][2])
            self.planmod.set(respuesta[0][3])
            self.preciomod.set(respuesta[0][4])
            self.conmod.set(respuesta[0][5])
        else:
            self.codigomod.set('')
            self.partemod.set('')
            self.ubimod.set('')
            self.cantmod.set('')
            self.planmod.set('')
            self.preciomod.set('')
            self.conmod.set('')
            mb.showinfo("Información", "No existe dato con dicho código")
            
    def modifica1(self):
        datos=(self.partemod.get(), self.ubimod.get(), self.cantmod.get(), self.planmod.get(), self.preciomod.get(), self.conmod.get(), self.codigomod.get())
        cantidad=self.inventariodb.modificacion1(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se actualizaron los datos correctamente")
            self.codigomod.set('')
            self.partemod.set('')
            self.ubimod.set('')
            self.cantmod.set('')
            self.planmod.set('')
            self.preciomod.set('')
            self.conmod.set('')
        else:
            mb.showinfo("Información", "No existe dato con dicho código")
            
    def modifica2(self):
        datos=(self.partemod.get(), self.ubimod.get(), self.cantmod.get(), self.planmod.get(), self.preciomod.get(), self.conmod.get(), self.codigomod.get())
        cantidad=self.inventariodb.modificacion2(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se actualizaron los datos correctamente")
            self.codigomod.set('')
            self.partemod.set('')
            self.ubimod.set('')
            self.cantmod.set('')
            self.planmod.set('')
            self.preciomod.set('')
            self.conmod.set('')
        else:
            mb.showinfo("Información", "No existe dato con dicho código")
            
    def modifica3(self):
        datos=(self.partemod.get(), self.ubimod.get(), self.cantmod.get(), self.planmod.get(), self.preciomod.get(), self.conmod.get(), self.codigomod.get())
        cantidad=self.inventariodb.modificacion3(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se actualizaron los datos correctamente")
            self.codigomod.set('')
            self.partemod.set('')
            self.ubimod.set('')
            self.cantmod.set('')
            self.planmod.set('')
            self.preciomod.set('')
            self.conmod.set('')
        else:
            mb.showinfo("Información", "No existe dato con dicho código")
            
    def modifica4(self):
        datos=(self.partemod.get(), self.ubimod.get(), self.cantmod.get(), self.planmod.get(), self.preciomod.get(), self.conmod.get(), self.codigomod.get())
        cantidad=self.inventariodb.modificacion4(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se actualizaron los datos correctamente")
            self.codigomod.set('')
            self.partemod.set('')
            self.ubimod.set('')
            self.cantmod.set('')
            self.planmod.set('')
            self.preciomod.set('')
            self.conmod.set('')
        else:
            mb.showinfo("Información", "No existe dato con dicho código")
            
    def modifica5(self):
        datos=(self.partemod.get(), self.ubimod.get(), self.cantmod.get(), self.planmod.get(), self.preciomod.get(), self.conmod.get(), self.codigomod.get())
        cantidad=self.inventariodb.modificacion5(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se actualizaron los datos correctamente")
            self.codigomod.set('')
            self.partemod.set('')
            self.ubimod.set('')
            self.cantmod.set('')
            self.planmod.set('')
            self.preciomod.set('')
            self.conmod.set('')
        else:
            mb.showinfo("Información", "No existe dato con dicho código")
            
            
    def borrar1(self):
           datos=(self.codigoborra.get(), )
           cantidad=self.inventariodb.baja1(datos)
           if cantidad==1:
               mb.showinfo("Información", "Se eliminó correctamente")
               self.codigoborra.set("")
           else:
               mb.showinfo("Información", "No existe dato con dicho código")
               self.codigoborra.set("")

    def borrar2(self):
           datos=(self.codigoborra.get(), )
           cantidad=self.inventariodb.baja2(datos)
           if cantidad==1:
               mb.showinfo("Información", "Se eliminó correctamente")
               self.codigoborra.set("")
           else:
               mb.showinfo("Información", "No existe dato con dicho código")
               self.codigoborra.set("")

    def borrar3(self):
           datos=(self.codigoborra.get(), )
           cantidad=self.inventariodb.baja3(datos)
           if cantidad==1:
               mb.showinfo("Información", "Se eliminó correctamente")
               self.codigoborra.set("")
           else:
               mb.showinfo("Información", "No existe dato con dicho código")
               self.codigoborra.set("")

    def borrar4(self):
           datos=(self.codigoborra.get(), )
           cantidad=self.inventariodb.baja4(datos)
           if cantidad==1:
               mb.showinfo("Información", "Se eliminó correctamente")
               self.codigoborra.set("")
           else:
               mb.showinfo("Información", "No existe dato con dicho código")
               self.codigoborra.set("")

    def borrar5(self):
           datos=(self.codigoborra.get(), )
           cantidad=self.inventariodb.baja5(datos)
           if cantidad==1:
               mb.showinfo("Información", "Se eliminó correctamente")
               self.codigoborra.set("")
           else:
               mb.showinfo("Información", "No existe dato con dicho código")
               self.codigoborra.set("")

def main():

    aplicacion1=Principal()
    return(0)

if __name__ == '__main__':
    main()
    



