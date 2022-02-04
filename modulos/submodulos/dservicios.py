from tkinter import *
from tkinter import messagebox
import tkinter as tk
from etc.funciones_varias import conectar_con_la_db
print("MODULO ACTIVO: {}" .format(__name__))

def dservicios():
    def añadir_a_la_base():
        db = "root.db"
        conn = conectar_con_la_db(db)
        cursor = conn.cursor()
        obproducto0 = servicion.get(ACTIVE)
        obproducto = obproducto0[0]
        if len(obproducto)<=1:
            return messagebox.showerror('Error', 'Valores no validos, ingrese nuevamente los valores')
        else:
            cursor.execute("select id from servicios where nombre=?",(obproducto,))
            data = cursor.fetchone()
            if(len(data)) > 0:
                cursor.execute("DELETE FROM servicios WHERE id=?", (data[0],))
                conn.commit()
                cursor.close()
                messagebox.showinfo('Eliminado', 'El servicio '+obproducto+' fue eliminado correctamente')
                return ventana_dservicios.destroy()
            else:
                return messagebox.showinfo('Error', 'El servicio '+obproducto+' no existe')

    if __name__ == "modulos.submodulos.dservicios":
        ventana_dservicios = tk.Toplevel()
        ventana_dservicios.grab_set()
        ventana_dservicios.focus_set
        banners3 = PhotoImage(file="img/banner_servicios.png")
        banners4 = banners3.subsample(3,2)
        titulo=Label(ventana_dservicios,image=banners4,compound=LEFT)
        titulo.place(x=60, y=10)
        #Obtener db
        db = "root.db"
        conn = conectar_con_la_db(db)
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM servicios order by id")
        data=cursor.fetchall()
        servicion_label = Label(ventana_dservicios, text="Seleccione el servicio:")
        servicion_label.place(x=20, y=100)
        scrollbar = Scrollbar(ventana_dservicios)
        scrollbar.pack(side=RIGHT, fill=Y)
        servicion = Listbox(ventana_dservicios)
        servicion.pack()
        for data in data:
            servicion.insert(END, data)
        servicion.config(yscrollcommand=scrollbar.set, height=5, selectmode=SINGLE, width=20)
        scrollbar.config(command=servicion.yview)
        servicion.place(x=150, y=100)
        ##Boton AÑADIR
        photoa = PhotoImage(file="img/delete_icon.png")  
        btn=Button(ventana_dservicios, text="Eliminar", fg='red', command=añadir_a_la_base, image=photoa,compound=LEFT)
        btn.place(x=30, y=350)
        ##Boton salir
        photoe = PhotoImage(file="img/exit_icon.png")  
        btn=Button(ventana_dservicios, text="Salir", command=ventana_dservicios.destroy, image=photoe,compound=LEFT)
        btn.place(x=300, y=350)
        ventana_dservicios.title('Eliminar servicio') #Titulo de la ventana principal
        ventana_dservicios.geometry("400x400") #Altura y anchura
        ventana_dservicios['bg'] = '#49A'
        ventana_dservicios.mainloop()
    return False