# -*- coding: utf-8 -*-
# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import sqlite3

class inventario:

    def abrir1(self):
        conexion1=sqlite3.connect("maq1.db")
        return conexion1
        
    def abrir2(self):
        conexion1=sqlite3.connect("maq2.db")
        return conexion1
    
    def abrir3(self):
        conexion1=sqlite3.connect("maq3.db")
        return conexion1
        
    def abrir4(self):
        conexion1=sqlite3.connect("maq4.db")
        return conexion1
        
    def abrir5(self):
        conexion1=sqlite3.connect("maq5.db")
        return conexion1


    def alta1(self, datos):
        cone=self.abrir1()
        cursor=cone.cursor()
        sql1="insert into maq1(parte, ubi, cant, plan, precio, con) values (?,?,?,?,?,?)"
        cursor.execute(sql1, datos)
        cone.commit()
        cone.close()
    
    def alta2(self, datos1):
        cone=self.abrir2()
        cursor=cone.cursor()
        sql2="insert into maq2(parte, ubi, cant, plan, precio, con) values (?,?,?,?,?,?)"
        cursor.execute(sql2, datos1)
        cone.commit()
        cone.close()
   
    def alta3(self, datos):
        cone=self.abrir3()
        cursor=cone.cursor()
        sql3="insert into maq3(parte, ubi, cant, plan, precio, con) values (?,?,?,?,?,?)"
        cursor.execute(sql3, datos)
        cone.commit()
        cone.close()
        
    def alta4(self, datos):
        cone=self.abrir4()
        cursor=cone.cursor()
        sql4="insert into maq4(parte, ubi, cant, plan, precio, con) values (?,?,?,?,?,?)"
        cursor.execute(sql4, datos)
        cone.commit()
        cone.close()
        
    def alta5(self, datos):
        cone=self.abrir5()
        cursor=cone.cursor()
        sql5="insert into maq5(parte, ubi, cant, plan, precio, con) values (?,?,?,?,?,?)"
        cursor.execute(sql5, datos)
        cone.commit()
        cone.close()
        
    def baja1(self, datos):
        try:
            cone=self.abrir1()
            cursor=cone.cursor()
            sql1="delete from maq1 where codigo=?"
            cursor.execute(sql1, datos)
            cone.commit()
            return cursor.rowcount
        except:
            cone.close()
            
    def baja2(self, datos):
        try:
            cone=self.abrir2()
            cursor=cone.cursor()
            sql2="delete from maq2 where codigo=?"
            cursor.execute(sql2, datos)
            cone.commit()
            return cursor.rowcount
        except:
            cone.close()
            
    def baja3(self, datos):
        try:
            cone=self.abrir3()
            cursor=cone.cursor()
            sql3="delete from maq3 where codigo=?"
            cursor.execute(sql3, datos)
            cone.commit()
            return cursor.rowcount
        except:
            cone.close()
            
    def baja4(self, datos):
        try:
            cone=self.abrir4()
            cursor=cone.cursor()
            sql4="delete from maq4 where codigo=?"
            cursor.execute(sql4, datos)
            cone.commit()
            return cursor.rowcount
        except:
            cone.close()
            
    def baja5(self, datos):
        try:
            cone=self.abrir5()
            cursor=cone.cursor()
            sql5="delete from maq5 where codigo=?"
            cursor.execute(sql5, datos)
            cone.commit()
            return cursor.rowcount
        except:
            cone.close()

    def view1(self):
        try:
            cone=self.abrir1()
            cursor=cone.cursor()
            sql1="select codigo, parte, ubi, cant, plan, precio, con from maq1"
            cursor.execute(sql1)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def view2(self):
        try:
            cone=self.abrir2()
            cursor=cone.cursor()
            sql2="select codigo, parte, ubi, cant, plan, precio, con from maq2"
            cursor.execute(sql2)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def view3(self):
        try:
            cone=self.abrir3()
            cursor=cone.cursor()
            sql1="select codigo, parte, ubi, cant, plan, precio, con from maq3"
            cursor.execute(sql1)
            return cursor.fetchall()
        finally:
            cone.close()

    def view4(self):
        try:
            cone=self.abrir4()
            cursor=cone.cursor()
            sql1="select codigo, parte, ubi, cant, plan, precio, con from maq4"
            cursor.execute(sql1)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def view5(self):
        try:
            cone=self.abrir5()
            cursor=cone.cursor()
            sql1="select codigo, parte, ubi, cant, plan, precio, con from maq5"
            cursor.execute(sql1)
            return cursor.fetchall()
        finally:
            cone.close()

    def consulta1(self, datos):
        try:
            cone=self.abrir1()
            cursor=cone.cursor()
            sql1="select parte, ubi, cant, plan, precio, con from maq1 where codigo=?"
            cursor.execute(sql1, datos)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def consulta2(self, datos):
        try:
            cone=self.abrir2()
            cursor=cone.cursor()
            sql1="select parte, ubi, cant, plan, precio, con from maq2 where codigo=?"
            cursor.execute(sql1, datos)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def consulta3(self, datos):
        try:
            cone=self.abrir3()
            cursor=cone.cursor()
            sql1="select parte, ubi, cant, plan, precio, con from maq3 where codigo=?"
            cursor.execute(sql1, datos)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def consulta4(self, datos):
        try:
            cone=self.abrir4()
            cursor=cone.cursor()
            sql1="select parte, ubi, cant, plan, precio, con from maq4 where codigo=?"
            cursor.execute(sql1, datos)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def consulta5(self, datos):
        try:
            cone=self.abrir5()
            cursor=cone.cursor()
            sql1="select parte, ubi, cant, plan, precio, con from maq5 where codigo=?"
            cursor.execute(sql1, datos)
            return cursor.fetchall()
        finally:
            cone.close()
                        
    def modificacion1(self, datos):
           try:
               cone=self.abrir1()
               cursor=cone.cursor()
               sql="update maq1 set parte=?, ubi=?, cant=?, plan=?, precio=?, con=? where codigo=?"
               cursor.execute(sql, datos)
               cone.commit()
               return cursor.rowcount
           except:
               cone.close()
               
    def modificacion2(self, datos):
           try:
               cone=self.abrir2()
               cursor=cone.cursor()
               sql="update maq2 set parte=?, ubi=?, cant=?, plan=?, precio=?, con=? where codigo=?"
               cursor.execute(sql, datos)
               cone.commit()
               return cursor.rowcount
           except:
               cone.close()
               
    def modificacion3(self, datos):
           try:
               cone=self.abrir3()
               cursor=cone.cursor()
               sql="update maq3 set parte=?, ubi=?, cant=?, plan=?, precio=?, con=? where codigo=?"
               cursor.execute(sql, datos)
               cone.commit()
               return cursor.rowcount
           except:
               cone.close()
               
    def modificacion4(self, datos):
           try:
               cone=self.abrir4()
               cursor=cone.cursor()
               sql="update maq4 set parte=?, ubi=?, cant=?, plan=?, precio=?, con=? where codigo=?"
               cursor.execute(sql, datos)
               cone.commit()
               return cursor.rowcount
           except:
               cone.close()
               
    def modificacion5(self, datos):
           try:
               cone=self.abrir5()
               cursor=cone.cursor()
               sql="update maq5 set parte=?, ubi=?, cant=?, plan=?, precio=?, con=? where codigo=?"
               cursor.execute(sql, datos)
               cone.commit()
               return cursor.rowcount
           except:
               cone.close()
               
    def recuperar_todos1(self):
        try:
            cone=self.abrir1()
            cursor=cone.cursor()
            sql="select codigo, parte, ubi, cant, plan, precio, con from maq1"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def recuperar_todos2(self):
        try:
            cone=self.abrir2()
            cursor=cone.cursor()
            sql="select codigo, parte, ubi, cant, plan, precio, con from maq2"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def recuperar_todos3(self):
        try:
            cone=self.abrir3()
            cursor=cone.cursor()
            sql="select codigo, parte, ubi, cant, plan, precio, con from maq3"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def recuperar_todos4(self):
        try:
            cone=self.abrir4()
            cursor=cone.cursor()
            sql="select codigo, parte, ubi, cant, plan, precio, con from maq4"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def recuperar_todos5(self):
        try:
            cone=self.abrir5()
            cursor=cone.cursor()
            sql="select codigo, parte, ubi, cant, plan, precio, con from maq5"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()
