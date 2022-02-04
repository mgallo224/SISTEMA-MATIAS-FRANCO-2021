from tkinter import *
from tkinter import messagebox
import tkinter as tk
from etc.funciones_varias import conectar_con_la_db
print("MODULO ACTIVO: {}" .format(__name__))

def dusers():
    def añadir_a_la_base():
        db = "root.db"
        conn = conectar_con_la_db(db)
        cursor = conn.cursor()
        obuser = user.get(ACTIVE)
        obuser = obuser[0]
        cursor.execute("select dni from empleados where legajo=?",(obuser,))
        data = cursor.fetchone()
        if(len(data)) > 0:
            cursor.execute("DELETE FROM empleados WHERE dni=?", (data[0],))
            conn.commit()
            cursor.close()
            messagebox.showinfo('Eliminado', 'El empleado fue eliminado correctamente')
            return ventana_dusers.destroy()
        else:
            return messagebox.showinfo('Error', 'El empleado no existe')

    if __name__ == "modulos.submodulos.dusers":
        ventana_dusers = tk.Toplevel()
        ventana_dusers.grab_set()
        ventana_dusers.focus_set
        banners3 = PhotoImage(file="img/banner_u.png")
        banners4 = banners3.subsample(3,2)
        titulo=Label(ventana_dusers,image=banners4,compound=LEFT)
        titulo.place(x=60, y=10)
        #Obtener db
        db = "root.db"
        conn = conectar_con_la_db(db)
        cursor = conn.cursor()
        cursor.execute("SELECT legajo FROM empleados order by legajo DESC")
        data=cursor.fetchall()
        user_label = Label(ventana_dusers, text="Seleccione el legajo:")
        user_label.place(x=20, y=100)
        scrollbar = Scrollbar(ventana_dusers)
        scrollbar.pack(side=RIGHT, fill=Y)
        user = Listbox(ventana_dusers)
        user.pack()
        for data in data:
            user.insert(END, data)
        user.config(yscrollcommand=scrollbar.set, height=5, selectmode=SINGLE, width=20)
        scrollbar.config(command=user.yview)
        user.place(x=150, y=100)
        ##Boton AÑADIR
        photoa = PhotoImage(file="img/delete_icon.png")  
        btn=Button(ventana_dusers, text="Eliminar", fg='red', command=añadir_a_la_base, image=photoa,compound=LEFT)
        btn.place(x=30, y=350)
        ##Boton salir
        photoe = PhotoImage(file="img/exit_icon.png")  
        btn=Button(ventana_dusers, text="Salir", command=ventana_dusers.destroy, image=photoe,compound=LEFT)
        btn.place(x=300, y=350)
        ventana_dusers.title('Eliminar empleado') #Titulo de la ventana principal
        ventana_dusers.geometry("400x400") #Altura y anchura
        ventana_dusers['bg'] = '#f4c20d'
        ventana_dusers.mainloop()
    return False