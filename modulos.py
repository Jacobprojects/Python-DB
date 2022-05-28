# -*- coding: utf-8 -*-
# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import carac


class Captura:
    def __init__(self):
        self.caracteristica1=carac.carac()
        self.ventana1=tk.Tk()
        self.ventana1.title("Captura de Alternativas")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.carga_caracteristicas()
        self.listado_completo()
        self.modificar()
        self.borrado()
        self.modelos()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def carga_caracteristicas(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Capturar")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Agregar Alternativa")
        self.labelframe1.grid(column=8, row=0, padx=5, pady=10)
        
        self.label0=ttk.Label(self.labelframe1, text="Nombre:")
        self.label0.grid(column=0, row=0, padx=4, pady=4)
        self.nombre=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe1, textvariable=self.nombre)
        self.entrynombre.grid(column=1, row=0, padx=4, pady=4)
        
        self.label1=ttk.Label(self.labelframe1, text="Peso Aeronave (Kg):")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.caracteristica1carga=tk.StringVar()
        self.entrycaracteristica1=ttk.Entry(self.labelframe1, textvariable=self.caracteristica1carga)
        self.entrycaracteristica1.grid(column=1, row=1, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Autonomia (Minutos):")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.caracteristica2carga=tk.StringVar()
        self.entrycaracteristica2=ttk.Entry(self.labelframe1, textvariable=self.caracteristica2carga)
        self.entrycaracteristica2.grid(column=1, row=2, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe1, text="Motores:")
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.caracteristica3carga=tk.StringVar()
        self.entrycaracteristica3=ttk.Entry(self.labelframe1, textvariable=self.caracteristica3carga)
        self.entrycaracteristica3.grid(column=1, row=3, padx=4, pady=4)
        
        self.label4=ttk.Label(self.labelframe1, text="Area de Vuelo (Metros):")
        self.label4.grid(column=0, row=4, padx=4, pady=4)
        self.caracteristica4carga=tk.StringVar()
        self.entrycaracteristica4=ttk.Entry(self.labelframe1, textvariable=self.caracteristica4carga)
        self.entrycaracteristica4.grid(column=1, row=4, padx=4, pady=4)
        
        self.label5=ttk.Label(self.labelframe1, text="Tecnologia:")
        self.label5.grid(column=0, row=5, padx=4, pady=4)
        self.caracteristica5carga=tk.StringVar()
        self.entrycaracteristica5=ttk.Entry(self.labelframe1, textvariable=self.caracteristica5carga)
        self.entrycaracteristica5.grid(column=1, row=5, padx=4, pady=4)
        
        self.label6=ttk.Label(self.labelframe1, text="Velocidad de Vuelo (Km/h):")
        self.label6.grid(column=0, row=6, padx=4, pady=4)
        self.caracteristica6carga=tk.StringVar()
        self.entrycaracteristica6=ttk.Entry(self.labelframe1, textvariable=self.caracteristica6carga)
        self.entrycaracteristica6.grid(column=1, row=6, padx=4, pady=4)
        
        self.label7=ttk.Label(self.labelframe1, text="Resistencia al Viento (Km/h):")
        self.label7.grid(column=0, row=7, padx=4, pady=4)
        self.caracteristica7carga=tk.StringVar()
        self.entrycaracteristica7=ttk.Entry(self.labelframe1, textvariable=self.caracteristica7carga)
        self.entrycaracteristica7.grid(column=1, row=7, padx=4, pady=4)
        
        self.label8=ttk.Label(self.labelframe1, text="Camara (Mp):")
        self.label8.grid(column=0, row=8, padx=4, pady=4)
        self.caracteristica8carga=tk.StringVar()
        self.entrycaracteristica8=ttk.Entry(self.labelframe1, textvariable=self.caracteristica8carga)
        self.entrycaracteristica8.grid(column=1, row=8, padx=4, pady=4)
        
        self.label9=ttk.Label(self.labelframe1, text="Precio ($):")
        self.label9.grid(column=0, row=9, padx=4, pady=4)
        self.preciocarga=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=9, padx=4, pady=4)
        
        
        self.boton1=ttk.Button(self.labelframe1, text="Agregar", command=self.agregar)
        self.boton1.grid(column=4, row=9, padx=4, pady=4)
        
        self.boton2=ttk.Button(self.labelframe1, text="Salir", command=quit)
        self.boton2.grid(column=5, row=9, padx=4, pady=4)
        

    def agregar(self):
        datos=(self.nombre.get(), self.caracteristica1carga.get(), self.caracteristica2carga.get(), self.caracteristica3carga.get(), self.caracteristica4carga.get(), self.caracteristica5carga.get(), self.caracteristica6carga.get(), self.caracteristica7carga.get(), self.caracteristica8carga.get(), self.preciocarga.get())
        self.caracteristica1.alta(datos)
        mb.showinfo("Información", "Los datos fueron agregados correctamente")
        self.nombre.set("")
        self.caracteristica1carga.set("")
        self.caracteristica2carga.set("")
        self.caracteristica3carga.set("")
        self.caracteristica4carga.set("")
        self.caracteristica5carga.set("")
        self.caracteristica6carga.set("")
        self.caracteristica7carga.set("")
        self.caracteristica8carga.set("")
        self.preciocarga.set("")
        


    def listado_completo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consultar")
        
        self.labelframe1=ttk.LabelFrame(self.pagina2, text="")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.tree= ttk.Treeview(self.labelframe1, column=("column1", "column2", "column3", "column4", "column5", "column6", "column7", "column8", "column9", "column10", "column11", ), show='headings')
        self.tree.grid(column=0, row=0, padx=5, pady=10)
        self.tree.heading("#1", text="Codigo", anchor=tk.S)
        self.tree.column("#1", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#2", text="Nombre", anchor=tk.S)
        self.tree.column("#2", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#3", text="Peso (Kg)", anchor=tk.S)
        self.tree.column("#3", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#4", text="Autonomia (Minutos)", anchor=tk.S)
        self.tree.column("#4", width=120, minwidth=70, stretch=tk.NO)
        self.tree.heading("#5", text="Motores", anchor=tk.S)
        self.tree.column("#5", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#6", text="Distancia (Metros)", anchor=tk.S)
        self.tree.column("#6", width=120, minwidth=70, stretch=tk.NO)
        self.tree.heading("#7", text="Tecnologia", anchor=tk.S)
        self.tree.column("#7", width=70, minwidth=70, stretch=tk.NO)
        self.tree.heading("#8", text="Velocidad (Km/h)", anchor=tk.S)
        self.tree.column("#8", width=120, minwidth=70, stretch=tk.NO)
        self.tree.heading("#9", text="Resistencia (Km/h)", anchor=tk.S)
        self.tree.column("#9", width=120, minwidth=70, stretch=tk.NO)
        self.tree.heading("#10", text="Camara (Mp)", anchor=tk.S)
        self.tree.column("#10", width=90, minwidth=70, stretch=tk.NO)
        self.tree.heading("#11", text="Precio", anchor=tk.S)
        self.tree.column("#11", width=70, minwidth=70, stretch=tk.NO)
        
        self.boton1=ttk.Button(self.labelframe1, text="Consultar", command=self.listar)
        self.boton1.grid(column=0, row=2, padx=4, pady=4)
        

    def listar(self):
        respuesta=self.caracteristica1.view()
        self.tree.delete(*self.tree.get_children())
        for row in respuesta:
            self.tree.insert("", tk.END, values=row)
        
    def modificar(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Modificar/Actualizar")
        self.labelframe1=ttk.LabelFrame(self.pagina3, text="")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigomod=tk.StringVar()
        self.entrycod=ttk.Entry(self.labelframe1, textvariable=self.codigomod)
        self.entrycod.grid(column=1, row=0, padx=4, pady=4)
        
        self.label11=ttk.Label(self.labelframe1, text="Nombre:")
        self.label11.grid(column=0, row=1, padx=4, pady=4)
        self.nombremod=tk.StringVar()
        self.entrynom=ttk.Entry(self.labelframe1, textvariable=self.nombremod)
        self.entrynom.grid(column=1, row=1, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Peso Aeronave (Kg):")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.caracteristica1mod=tk.StringVar()
        self.entrycaracteristica1=ttk.Entry(self.labelframe1, textvariable=self.caracteristica1mod)
        self.entrycaracteristica1.grid(column=1, row=2, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe1, text="Autonomia (Minutos):")
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.caracteristica2mod=tk.StringVar()
        self.entrycaracteristica2=ttk.Entry(self.labelframe1, textvariable=self.caracteristica2mod)
        self.entrycaracteristica2.grid(column=1, row=3, padx=4, pady=4)
        
        self.label4=ttk.Label(self.labelframe1, text="Motores:")
        self.label4.grid(column=0, row=4, padx=4, pady=4)
        self.caracteristica3mod=tk.StringVar()
        self.entrycaracteristica3=ttk.Entry(self.labelframe1, textvariable=self.caracteristica3mod)
        self.entrycaracteristica3.grid(column=1, row=4, padx=4, pady=4)
        
        self.label5=ttk.Label(self.labelframe1, text="Area de Vuelo (Metros):")
        self.label5.grid(column=0, row=5, padx=4, pady=4)
        self.caracteristica4mod=tk.StringVar()
        self.entrycaracteristica4=ttk.Entry(self.labelframe1, textvariable=self.caracteristica4mod)
        self.entrycaracteristica4.grid(column=1, row=5, padx=4, pady=4)
        
        self.label6=ttk.Label(self.labelframe1, text="Tecnologia:")
        self.label6.grid(column=0, row=6, padx=4, pady=4)
        self.caracteristica5mod=tk.StringVar()
        self.entrycaracteristica5=ttk.Entry(self.labelframe1, textvariable=self.caracteristica5mod)
        self.entrycaracteristica5.grid(column=1, row=6, padx=4, pady=4)
        
        self.label7=ttk.Label(self.labelframe1, text="Velocidad de Vuelo (Km/h):")
        self.label7.grid(column=0, row=7, padx=4, pady=4)
        self.caracteristica6mod=tk.StringVar()
        self.entrycaracteristica6=ttk.Entry(self.labelframe1, textvariable=self.caracteristica6mod)
        self.entrycaracteristica6.grid(column=1, row=7, padx=4, pady=4)
        
        self.label8=ttk.Label(self.labelframe1, text="Resistencia al Viento (Km/h):")
        self.label8.grid(column=0, row=8, padx=4, pady=4)
        self.caracteristica7mod=tk.StringVar()
        self.entrycaracteristica7=ttk.Entry(self.labelframe1, textvariable=self.caracteristica7mod)
        self.entrycaracteristica7.grid(column=1, row=8, padx=4, pady=4)
        
        self.label9=ttk.Label(self.labelframe1, text="Camara (Mp):")
        self.label9.grid(column=0, row=9, padx=4, pady=4)
        self.caracteristica8mod=tk.StringVar()
        self.entrycaracteristica8=ttk.Entry(self.labelframe1, textvariable=self.caracteristica8mod)
        self.entrycaracteristica8.grid(column=1, row=9, padx=4, pady=4)
        
        self.label10=ttk.Label(self.labelframe1, text="Precio:")
        self.label10.grid(column=0, row=10, padx=4, pady=4)
        self.preciomod=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=10, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe1, text="Buscar", command=self.consultar_mod)
        self.boton1.grid(column=1, row=11, padx=4, pady=4)
       
        self.boton2=ttk.Button(self.labelframe1, text="Actualizar", command=self.modifica)
        self.boton2.grid(column=1, row=12, padx=4, pady=4)

    def modifica(self):
        datos=(self.nombremod.get(), self.caracteristica1mod.get(), self.caracteristica2mod.get(), self.caracteristica3mod.get(), self.caracteristica4mod.get(), self.caracteristica5mod.get(), self.caracteristica6mod.get(), self.caracteristica7mod.get(), self.caracteristica8mod.get(), self.preciomod.get(), self.codigomod.get())
        cantidad=self.caracteristica1.modificacion(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se actualizaron los datos correctamente")
        else:
            mb.showinfo("Información", "No existe una alternativa con dicho código")

    def consultar_mod(self):
        datos=(self.codigomod.get(), )
        respuesta=self.caracteristica1.consulta(datos)
        if len(respuesta)>0:
            self.nombremod.set(respuesta[0][0])
            self.caracteristica1mod.set(respuesta[0][1])
            self.caracteristica2mod.set(respuesta[0][2])
            self.caracteristica3mod.set(respuesta[0][3])
            self.caracteristica4mod.set(respuesta[0][4])
            self.caracteristica5mod.set(respuesta[0][5])
            self.caracteristica6mod.set(respuesta[0][6])
            self.caracteristica7mod.set(respuesta[0][7])
            self.caracteristica8mod.set(respuesta[0][8])
            self.preciomod.set(respuesta[0][9])
        else:
            self.codigomod.set('')
            self.nombremod.set('')
            self.caracteristica1mod.set('')
            self.caracteristica2mod.set('')
            self.caracteristica3mod.set('')
            self.caracteristica4mod.set('')
            self.caracteristica5mod.set('')
            self.caracteristica6mod.set('')
            self.caracteristica7mod.set('')
            self.caracteristica8mod.set('')
            self.preciomod.set('')
            mb.showinfo("Información", "No existe una alternativa con dicho código")
            
    def borrado(self):
           self.pagina4 = ttk.Frame(self.cuaderno1)
           self.cuaderno1.add(self.pagina4, text="Eliminar")
           self.labelframe1=ttk.LabelFrame(self.pagina4, text="Eliminar alternativa")
           self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
           self.label1=ttk.Label(self.labelframe1, text="Código:")
           self.label1.grid(column=0, row=0, padx=4, pady=4)
           self.codigoborra=tk.StringVar()
           self.entryborra=ttk.Entry(self.labelframe1, textvariable=self.codigoborra)
           self.entryborra.grid(column=1, row=0, padx=4, pady=4)
           self.boton1=ttk.Button(self.labelframe1, text="Eliminar", command=self.borrar)
           self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
           datos=(self.codigoborra.get(), )
           cantidad=self.caracteristica1.baja(datos)
           if cantidad==1:
               mb.showinfo("Información", "Se borró la alternativa con dicho código")
           else:
               mb.showinfo("Información", "No existe alternativa con dicho código")
               
    def modelos(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Topsis")
        
        self.labelframe1=ttk.LabelFrame(self.pagina5, text="Selección Multicriterio")
        self.labelframe1.pack(fill="both", expand="yes")
        
        self.toplabel = ttk.Label(self.labelframe1, text="Aqui se muestran las matrices")
        self.toplabel1 = ttk.Label(self.labelframe1, text = "Nom. ")
        self.n=tk.StringVar()
        self.entryn=ttk.Entry(self.labelframe1, textvariable=self.n)
        self.toplabel2 = ttk.Label(self.labelframe1, text = "Car. 1")
        self.toplabel3 = ttk.Label(self.labelframe1, text = "Car. 2")
        self.toplabel4 = ttk.Label(self.labelframe1, text = "Car. 3")
        self.toplabel5 = ttk.Label(self.labelframe1, text = "Car. 4")
        self.toplabel6 = ttk.Label(self.labelframe1, text = "Car. 5")
        self.toplabel7 = ttk.Label(self.labelframe1, text = "Precio")
        self.toplabel.pack()
        self.entryn.pack()
        self.toplabel1.pack()
        self.toplabel2.pack()
        self.toplabel3.pack()
        self.toplabel4.pack()
        self.toplabel5.pack()
        self.toplabel6.pack()
        self.toplabel7.pack()
          
        self.labelframe2 = ttk.LabelFrame(self.pagina5, text = "Guión de Narrativa")
        self.labelframe2.pack(fill="both", expand = "yes")
          
        self.bottomlabel = ttk.Label(self.labelframe2,text = "Mostrar información acerca de TOPSIS")
        self.bottomlabel1 = ttk.Label(self.labelframe2, text = "Nom. ")
        self.bottomlabel2 = ttk.Label(self.labelframe2, text = "Car. 1")
        self.bottomlabel3 = ttk.Label(self.labelframe2, text = "Car. 2")
        self.bottomlabel4 = ttk.Label(self.labelframe2, text = "Car. 3")
        self.bottomlabel5 = ttk.Label(self.labelframe2, text = "Car. 4")
        self.bottomlabel6 = ttk.Label(self.labelframe2, text = "Car. 5")
        self.bottomlabel7 = ttk.Label(self.labelframe2, text = "Precio ")
        self.bottomlabel.pack()
        self.bottomlabel1.pack()
        self.bottomlabel2.pack()
        self.bottomlabel3.pack()
        self.bottomlabel4.pack()
        self.bottomlabel5.pack()
        self.bottomlabel6.pack()
        self.bottomlabel7.pack()
        
        
        
        

aplicacion1=Captura()
