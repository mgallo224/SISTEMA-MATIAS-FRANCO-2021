from tkinter import *
from tkinter import messagebox
import tkinter as tk
from etc.funciones_varias import conectar_con_la_db
print("MODULO ACTIVO: {}" .format(__name__))

def dstock():
    def añadir_a_la_base():
        db = "root.db"
        conn = conectar_con_la_db(db)
        cursor = conn.cursor()
        obproducto0 = producto.get(ACTIVE)
        obproducto = obproducto0[0]
        if len(obproducto)<=1:
            return messagebox.showerror('Error', 'Valores no validos, ingrese nuevamente los valores')
        else:
            cursor.execute("select id from stock where producto=?",(obproducto,))
            data = cursor.fetchone()
            if(len(data)) > 0:
                cursor.execute("DELETE FROM stock WHERE id=?", (data[0],))
                conn.commit()
                cursor.close()
                messagebox.showinfo('Eliminado', 'El producto '+obproducto+' fue eliminado correctamente del stock')
                return ventana_dstock.destroy()
            else:
                return messagebox.showinfo('Error', 'El producto '+obproducto+' no existe en el stock')

    if __name__ == "modulos.submodulos.dstock":
        ventana_dstock = tk.Toplevel()
        ventana_dstock.grab_set()
        ventana_dstock.focus_set
        banners3 = PhotoImage(file="img/banner_stock.png")
        banners4 = banners3.subsample(3,2)
        titulo=Label(ventana_dstock,image=banners4,compound=LEFT)
        titulo.place(x=60, y=10)
        #Obtener db
        db = "root.db"
        conn = conectar_con_la_db(db)
        cursor = conn.cursor()
        cursor.execute("SELECT producto FROM stock order by id")
        data=cursor.fetchall()
        producto_label = Label(ventana_dstock, text="Seleccione el producto:")
        producto_label.place(x=20, y=100)
        scrollbar = Scrollbar(ventana_dstock)
        scrollbar.pack(side=RIGHT, fill=Y)
        producto = Listbox(ventana_dstock)
        producto.pack()
        for data in data:
            producto.insert(END, data)
        producto.config(yscrollcommand=scrollbar.set, height=5, selectmode=SINGLE, width=20)
        scrollbar.config(command=producto.yview)
        producto.place(x=150, y=100)
        ##Boton AÑADIR
        photoa = PhotoImage(file="img/delete_icon.png")  
        btn=Button(ventana_dstock, text="Eliminar", fg='red', command=añadir_a_la_base, image=photoa,compound=LEFT)
        btn.place(x=30, y=350)
        ##Boton salir
        photoe = PhotoImage(file="img/exit_icon.png")  
        btn=Button(ventana_dstock, text="Salir", command=ventana_dstock.destroy, image=photoe,compound=LEFT)
        btn.place(x=300, y=350)
        ventana_dstock.title('Eliminar stock') #Titulo de la ventana principal
        ventana_dstock.geometry("400x400") #Altura y anchura
        ventana_dstock['bg'] = '#833AB4'
        ventana_dstock.mainloop()
    return False