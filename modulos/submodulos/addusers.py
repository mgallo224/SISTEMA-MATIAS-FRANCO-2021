from os import name
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from etc.funciones_varias import conectar_con_la_db,fechayhora
print("MODULO ACTIVO: {}" .format(__name__))


def addusers():
    def añadir_a_la_base():
        db = "root.db"
        conn = conectar_con_la_db(db)
        cursor = conn.cursor()
        nuser0 = nuser.get()
        obnuser = nuser0.capitalize()
        auser0 = auser.get()
        obauser = auser0.capitalize()
        obcargo = cargo.get(ACTIVE)
        fecha = fechayhora()
        cursor.execute("select max(legajo) from empleados")
        legajo = cursor.fetchone()
        dni = dniuser.get()
        obsueldo = sueldo.get()
        cursor.execute("select dni from empleados where dni=?",(dni,))
        data = cursor.fetchone()
        if len(obnuser)<=0 or len(obauser)<=0 or len(obcargo)<=0 or obnuser.isnumeric() == True or obauser.isnumeric() == True or obcargo.isnumeric() == True or dni.isnumeric() == False:
            return messagebox.showerror('Error', 'Valores no validos, ingrese nuevamente los valores')
        elif (data is None) == False:
            return messagebox.showerror("Error", "El empleado ya esta agregado")
        elif  obsueldo.isnumeric() == False:
            return messagebox.showerror('Error', 'El sueldo debe ser numerico')  
        elif int(obsueldo)<=0:
            return messagebox.showerror('Error', 'Error al ingresar datos por favor corrigalos y vuelva a ingresarlos')
        elif len(dni)<=0 or len(dni)!=8: 
            return messagebox.showerror('Error', 'Dni incorrecto')
        else:
            if (legajo[0] is None) == True:
                alegajo = 1
            else:
                alegajo = legajo[0]+1
            cursor.execute("insert into empleados (dni,nombre,apellido,jerarquia,legajo,fecha,sueldo) values (?,?, ?, ?, ?, ? , ?)",(dni,obnuser,obauser,obcargo,alegajo,fecha,obsueldo))
            conn.commit()
            cursor.close()
            messagebox.showinfo('Añadido', 'El empleado '+obnuser+' '+obauser+' fue añadido correctamente con el legajo: '+str(alegajo))
            return dniuser.delete(0,END),nuser.delete(0,END),auser.delete(0,END),sueldo.delete(0,END),cargo.selection_clear(0, tk.END)

    if __name__ == "modulos.submodulos.addusers":
        ventana_addusers = tk.Toplevel()
        ventana_addusers.grab_set()
        ventana_addusers.focus_set
        banners3 = PhotoImage(file="img/banner_u.png")
        banners4 = banners3.subsample(3,2)
        titulo=Label(ventana_addusers,image=banners4,compound=LEFT)
        titulo.place(x=60, y=10)
        # Crear caja de texto nombre
        dniuser_label = Label(ventana_addusers, text="DNI:")
        dniuser_label.place(x=20, y=100)
        dniuser = tk.Entry(ventana_addusers)
        # Posicionarla en la ventana.
        dniuser.place(x=100, y=100)
        # Crear caja de texto nombre
        nuser_label = Label(ventana_addusers, text="Nombre:")
        nuser_label.place(x=20, y=150)
        nuser = tk.Entry(ventana_addusers)
        # Posicionarla en la ventana.
        nuser.place(x=100, y=150)
        # Crear caja de texto apellido
        auser_label = Label(ventana_addusers, text="Apellido:")
        auser_label.place(x=20, y=200)
        auser = tk.Entry(ventana_addusers)
        # Posicionarla en la ventana.
        auser.place(x=100, y=200)
        # Crear caja de texto cargo
        cargor=["Cocina","Delivery","Encargado","Jefe de cocina","Limpieza","Atención al publico","Administración"]
        cargo_label = Label(ventana_addusers, text="Cargo:")
        cargo_label.place(x=20, y=250)
        scrollbar = Scrollbar(ventana_addusers)
        scrollbar.pack(side=RIGHT, fill=Y)
        cargo = Listbox(ventana_addusers)
        cargo.pack()
        for cargor in cargor:
            cargo.insert(END, cargor)
        cargo.config(yscrollcommand=scrollbar.set, height=5, selectmode=SINGLE, width=20)
        scrollbar.config(command=cargo.yview)
        cargo.place(x=100, y=250)
        # Crear caja de texto sueldo
        sueldo_label = Label(ventana_addusers, text="Sueldo ($):")
        sueldo_label.place(x=20, y=350)
        sueldo = tk.Entry(ventana_addusers)
        # Posicionarla en la ventana.
        sueldo.place(x=100, y=350)
        ##Boton AÑADIR
        photoa = PhotoImage(file="img/save_icon.png")  
        btn=Button(ventana_addusers, text="Dar de alta", fg='green', command=añadir_a_la_base, image=photoa,compound=LEFT)
        btn.place(x=30, y=450)
        ##Boton salir
        photoe = PhotoImage(file="img/exit_icon.png")  
        btn=Button(ventana_addusers, text="Salir", fg='red', command=ventana_addusers.destroy, image=photoe,compound=LEFT)
        btn.place(x=300, y=450)
        ventana_addusers.title('Agregar empleado') #Titulo de la ventana principal
        ventana_addusers.geometry("400x500") #Altura y anchura
        ventana_addusers['bg'] = '#f4c20d'
        ventana_addusers.mainloop()
    return False
