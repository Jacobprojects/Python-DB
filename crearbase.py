#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conexion1=sqlite3.connect("maq1.db")
try:
    conexion1.execute("""create table maq1 (
                              codigo integer primary key AUTOINCREMENT,
                              parte text,
                              ubi text,
                              cant text,
                              plan text,
                              precio text,
                              con text
                        )""")
    print("La base de datos #1 se creo correctamente.")
except sqlite3.OperationalError:
    print("La base de datos ya existe.")

conexion2=sqlite3.connect("maq2.db")
try:
    conexion2.execute("""create table maq2 (
                              codigo integer primary key AUTOINCREMENT,
                              parte text,
                              ubi text,
                              cant text,
                              plan text,
                              precio text,
                              con text
                        )""")
    print("La base de datos #2 se creo correctamente.")
except sqlite3.OperationalError:
    print("La base de datos ya existe.")
    
conexion3=sqlite3.connect("maq3.db")
try:
    conexion3.execute("""create table maq3 (
                              codigo integer primary key AUTOINCREMENT,
                              parte text,
                              ubi text,
                              cant text,
                              plan text,
                              precio text,
                              con text
                        )""")
    print("La base de datos #3 se creo correctamente.")
except sqlite3.OperationalError:
    print("La base de datos ya existe.")
    
conexion4=sqlite3.connect("maq4.db")
try:
    conexion4.execute("""create table maq4 (
                              codigo integer primary key AUTOINCREMENT,
                              parte text,
                              ubi text,
                              cant text,
                              plan text,
                              precio text,
                              con text
                        )""")
    print("La base de datos #4 se creo correctamente.")
except sqlite3.OperationalError:
    print("La base de datos ya existe.")
    
conexion5=sqlite3.connect("maq5.db")
try:
    conexion5.execute("""create table maq5 (
                              codigo integer primary key AUTOINCREMENT,
                              parte text,
                              ubi text,
                              cant text,
                              plan text,
                              precio text,
                              con text
                        )""")
    print("La base de datos #5 se creo correctamente.")
except sqlite3.OperationalError:
    print("La base de datos ya existe.")
    
conexion1.close()
conexion2.close()
conexion3.close()
conexion4.close()
conexion5.close()
