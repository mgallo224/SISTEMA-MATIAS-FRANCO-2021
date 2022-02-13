from tkinter import * 
import os
def fechayhora():
    from datetime import datetime
    fecha = datetime.today().strftime('%Y-%m-%d %H:%M')
    return fecha

def mes():
    from datetime import datetime
    mes = datetime.today().strftime('%m')
    return mes


def año():
    from datetime import datetime
    año = datetime.today().strftime('%Y')
    return año   

def conectar_con_la_db(db_file):
    import sqlite3
    from sqlite3 import Error
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def crear_directorio(nombre):
    if not os.path.exists(nombre):
        os.mkdir(nombre)
        print("Carpeta " , nombre ,  " Creada ")
    else:    
        print("Carpeta " , nombre,  " ya existe")
    return False

def crear_db():
        db = "root.db"
        conn = conectar_con_la_db(db)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS stock(id INTEGER PRIMARY KEY NOT NULL UNIQUE, producto TEXT, tipo TEXT, cantidad	INTEGER, fecha	TEXT, veces	INTEGER, vxunidad	INTEGER, costoxunidad INTEGER, costoxcantidad INTEGER,precioventa INTEGER)")
        cursor.execute("CREATE TABLE IF NOT EXISTS carrito( id INTEGER PRIMARY KEY NOT NULL UNIQUE, producto TEXT, cantidad INTEGER, precio NUMERIC, fecha TEXT,ncliente	TEXT,parallevar	INTEGER,dcliente	TEXT, mes NUMERIC, año NUMERIC,tipo TEXT,liquidacion NUMERIC)")
        cursor.execute("CREATE TABLE IF NOT EXISTS ventas( id INTEGER PRIMARY KEY NOT NULL UNIQUE, producto TEXT, cantidad INTEGER, precio NUMERIC, fecha TEXT,ncliente	TEXT,parallevar	INTEGER,dcliente	TEXT, mes NUMERIC, año NUMERIC,tipo TEXT,liquidacion NUMERIC)")
        cursor.execute("CREATE TABLE IF NOT EXISTS empleados( DNI INTEGER PRIMARY KEY NOT NULL UNIQUE, nombre TEXT, apellido TEXT,jerarquia	TEXT,legajo	INTEGER,fecha TEXT,sueldo NUMERIC)")
        cursor.execute("CREATE TABLE IF NOT EXISTS servicios(id INTEGER PRIMARY KEY NOT NULL UNIQUE, nombre TEXT, tipo TEXT, gxmes	INTEGER, fecha	TEXT)")
        cursor.execute("DELETE FROM carrito")
        conn.commit()
        cursor.close()
        return False

def checkaño():
    import datetime
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    db = "root.db"
    conn = conectar_con_la_db(db)
    cursor = conn.cursor()
    cursor.execute("SELECT max(año) from ventas")
    data = cursor.fetchone()
    year = date.strftime("%Y")
    if int(year)!=data[0]:
        cursor.execute("DELETE FROM ventas WHERE año=?", (data[0],))
        conn.commit()
        cursor.close()
    return False

def llamar_a_admservicios():
    from modulos.admservicios import admservicios
    admservicios()

def llamar_a_aservicios():
    from modulos.submodulos.aservicios import aservicios
    aservicios()
    
def llamar_a_dservicios():
    from modulos.submodulos.dservicios import dservicios
    dservicios()

def llamar_a_vservicios():
    from modulos.submodulos.vservicios import vservicios
    vservicios()    

def llamar_a_cventas():
    from modulos.cventas import cventas
    cventas()
    
def llamar_a_admventas():
    from modulos.admventas import admventas
    admventas()

def llamar_a_buscarv():
    from modulos.submodulos.buscarv import buscarv
    buscarv()
    
def llamar_a_astock():
    from modulos.submodulos.astock import astock
    astock()

def llamar_a_dstock():
    from modulos.submodulos.dstock import dstock
    dstock()

def llamar_a_estock():
    from modulos.submodulos.estock import estock
    estock()

def llamar_a_admstock():
    from modulos.admstock import admstock
    admstock()

def llamar_a_vstock():
    from modulos.submodulos.vstock import vstock
    vstock()

def llamar_a_trending():
    from modulos.submodulos.trending import trending
    trending()

def llamar_a_admusers():
    from modulos.admusers import admusers
    admusers()

def llamar_a_addusers():
    from modulos.submodulos.addusers import addusers
    addusers()

def llamar_a_vusers():
    from modulos.submodulos.vusers import vusers
    vusers()

def llamar_a_dusers():
    from modulos.submodulos.dusers import dusers
    dusers()

def llamar_a_eusers():
    from modulos.submodulos.eusers import eusers
    eusers()
    
def llamar_a_calc():
    from modulos.submodulos.calc import calc
    calc()