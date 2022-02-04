from tkinter import *
from tkinter import messagebox
import tkinter as tk
from etc.funciones_varias import conectar_con_la_db
print("MODULO ACTIVO: {}" .format(__name__))

def eusers():
 if __name__ == "modulos.submodulos.eusers":
    def eusers2():
            def añadir_a_la_base():
                db = "root.db"
                conn = conectar_con_la_db(db)
                cursor = conn.cursor()
                obcargo = cargo.get(ACTIVE)
                obsueldo = sedit.get()
                if len(obcargo)<=0 or obcargo.isnumeric() == True:
                    return messagebox.showerror('Error', 'Valores no validos, ingrese nuevamente los valores')
                elif  obsueldo.isnumeric() == False:
                    return messagebox.showerror('Error', 'El sueldo debe ser numerico')  
                else:
                     if int(obsueldo)<=0:
                         return messagebox.showerror('Error', 'El sueldo debe ser mayor a 0')
                     else:
                        cursor.execute("UPDATE empleados SET jerarquia=? , sueldo=? where dni=?", (obcargo,obsueldo,data[2]))
                        conn.commit()
                        cursor.close()
                        messagebox.showinfo('Editado', 'El empleado fue editado correctamente')
                     return ventana_eusers.destroy(), ventana_eusers2.destroy()

            ventana_eusers2 = tk.Toplevel()
            ventana_eusers2.grab_set()
            ventana_eusers2.focus_set
            banners3 = PhotoImage(file="img/banner_u.png")
            banners4 = banners3.subsample(3,2)
            titulo=Label(ventana_eusers2,image=banners4,compound=LEFT)
            titulo.place(x=60, y=10)
            #Obtener db
            db = "root.db"
            conn = conectar_con_la_db(db)
            cursor = conn.cursor()
            obtener_legajo = legajo.get(ACTIVE)
            cursor.execute("SELECT jerarquia,sueldo,dni,nombre,apellido FROM empleados WHERE legajo = ?", (obtener_legajo[0],))
            data=cursor.fetchone()
            #TXT
            dni_label = Label(ventana_eusers2, text="DNI:  "+str(data[2]))
            dni_label.place(x=20, y=100)
            #TXT2
            name_label = Label(ventana_eusers2, text="Nombre:  "+str(data[3]))
            name_label.place(x=20, y=150)
            #TXT2
            apellido_label = Label(ventana_eusers2, text="Apellido:  "+str(data[4]))
            apellido_label.place(x=20, y=200)
            #cargo
            cargor=["Cocina","Delivery","Encargado","Jefe de cocina","Limpieza","Atención al publico","Administración"]
            cargo_label = Label(ventana_eusers2, text="Cargo:")
            cargo_label.place(x=20, y=250)
            scrollbar = Scrollbar(ventana_eusers2)
            scrollbar.pack(side=RIGHT, fill=Y)
            cargo = Listbox(ventana_eusers2)
            cargo.pack()
            for cargor in cargor:
                cargo.insert(END, cargor)
            cargo.config(yscrollcommand=scrollbar.set, height=5, selectmode=SINGLE, width=20)
            scrollbar.config(command=cargo.yview)
            cargo.place(x=100, y=250)
            #SUELDO
            sedit_label = Label(ventana_eusers2, text="Sueldo:")
            sedit_label.place(x=20, y=350)
            sedit = Entry(ventana_eusers2)
            sedit.insert(END, data[1])
            sedit.pack()
            sedit.place(x=100, y=350)  
            ##Boton AÑADIR
            photoa = PhotoImage(file="img/save_icon.png")  
            btn=Button(ventana_eusers2, text="Guardar cambios", fg='green', command=añadir_a_la_base, image=photoa,compound=LEFT)
            btn.place(x=30, y=450)
            ##Boton salir
            photoe = PhotoImage(file="img/exit_icon.png")  
            btn=Button(ventana_eusers2, text="Salir", fg="red", command=ventana_eusers2.destroy, image=photoe,compound=LEFT)
            btn.place(x=200, y=450)
            ventana_eusers2.title('Editar empleados') #Titulo de la ventana principal
            ventana_eusers2.geometry("300x500") #Altura y anchura
            ventana_eusers2['bg'] = '#f4c20d'
            ventana_eusers2.mainloop()
            return False
    ventana_eusers = tk.Toplevel()
    ventana_eusers.grab_set()
    ventana_eusers.focus_set
    banners3 = PhotoImage(file="img/banner_u.png")
    banners4 = banners3.subsample(3,2)
    titulo=Label(ventana_eusers,image=banners4,compound=LEFT)
    titulo.place(x=60, y=10)
    #Obtener db
    db = "root.db"
    conn = conectar_con_la_db(db)
    cursor = conn.cursor()
    cursor.execute("SELECT legajo FROM empleados order by legajo DESC")
    data=cursor.fetchall()
    legajo_label = Label(ventana_eusers, text="Legajo del empleado:")
    legajo_label.place(x=20, y=100)
    scrollbar = Scrollbar(ventana_eusers)
    scrollbar.pack(side=RIGHT, fill=Y)
    legajo = Listbox(ventana_eusers)
    legajo.pack()
    for data in data:
        legajo.insert(END, data)
    legajo.config(yscrollcommand=scrollbar.set, height=5, selectmode=SINGLE, width=20)
    scrollbar.config(command=legajo.yview)
    legajo.place(x=150, y=100)
    ##Boton AÑADIR
    photoa = PhotoImage(file="img/edit_icon.png")  
    btn=Button(ventana_eusers, text="Editar", fg='blue', command=eusers2, image=photoa,compound=LEFT)
    btn.place(x=30, y=350)
    ##Boton salir
    photoe = PhotoImage(file="img/exit_icon.png")  
    btn=Button(ventana_eusers, text="Salir", command=ventana_eusers.destroy, image=photoe,compound=LEFT)
    btn.place(x=300, y=350)
    ventana_eusers.title('Editar empleados') #Titulo de la ventana principal
    ventana_eusers.geometry("400x400") #Altura y anchura
    ventana_eusers['bg'] = '#f4c20d'
    ventana_eusers.mainloop()
    return False