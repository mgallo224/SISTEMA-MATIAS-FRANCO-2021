from tkinter import *
from tkinter import messagebox
import tkinter as tk
from etc.funciones_varias import conectar_con_la_db
print("MODULO ACTIVO: {}" .format(__name__))

def estock():
 if __name__ == "modulos.submodulos.estock":
    def estock2():
            def auto():
                if len(cedit.get() ) == 0 or len(cxuedit.get()) == 0 or cedit.get().isnumeric() == False or cxuedit.get().isnumeric() == False:
                    costo3_label['text'] = "0"
                else:
                    costo3_label['text'] = int(cedit.get())*int(cxuedit.get())
                    ventana_estock2.after(2000, auto)  
            def añadir_a_la_base():
                db = "root.db"
                conn = conectar_con_la_db(db)
                cursor = conn.cursor()
                obcantidad =  cedit.get() 
                obcostoxunidad =  cxuedit.get()
                obtipo = tipo.get(ACTIVE)
                cxcant = int(cedit.get())*int(cxuedit.get())
                obprecioventa = precio_a_vender.get()
                if len(obcantidad)<=0 or len(obtipo)<=0 or len(obcostoxunidad)<=0 or len(obprecioventa)<=0:
                    return messagebox.showerror('Error', 'Valores no validos, ingrese nuevamente los valores')
                elif  obcantidad.isnumeric() == False or obcostoxunidad.isnumeric() == False or obprecioventa.isnumeric() == False:
                    return messagebox.showerror('Error', 'La cantidad,el precio y el costo deben ser numericos')
                elif  int(obcantidad)<=0 or int(obcostoxunidad)<=0  or int(cxcant)<=0 or int(obprecioventa)<=0:
                    return messagebox.showerror('Error', 'La cantidad,el precio y el costo deben ser mayores a 0')
                else:
                    cursor.execute("UPDATE stock SET tipo=?, cantidad=?,costoxunidad=?,costoxcantidad=?  where id=?", (obtipo,obcantidad,obcostoxunidad,cxcant,data[0]))
                    conn.commit()
                    cursor.close()
                    messagebox.showinfo('Editado', 'El producto fue editado correctamente')
                    return ventana_estock.destroy(), ventana_estock2.destroy()

            ventana_estock2 = tk.Toplevel()
            ventana_estock2.grab_set()
            ventana_estock2.focus_set
            banners3 = PhotoImage(file="img/banner_stock.png")
            banners4 = banners3.subsample(3,2)
            titulo=Label(ventana_estock2,image=banners4,compound=LEFT)
            titulo.place(x=60, y=10)
            obtener_producto = producto.get(ACTIVE)
            cursor.execute("SELECT id,tipo,cantidad,costoxunidad,precioventa FROM stock WHERE producto = ?", (obtener_producto[0],))
            data=cursor.fetchone()
            #tipo
            tipor=["Bebida","Postre","Guarnición","Entrada","Pizzas","Empanadas","Pastas"]
            tipo_label = Label(ventana_estock2, text="Tipo:")
            tipo_label.place(x=20, y=100)
            scrollbar = Scrollbar(ventana_estock2)
            scrollbar.pack(side=RIGHT, fill=Y)
            tipo = Listbox(ventana_estock2)
            tipo.pack()
            for tipor in tipor:
                tipo.insert(END, tipor)
            tipo.config(yscrollcommand=scrollbar.set, height=5, selectmode=SINGLE, width=20)
            scrollbar.config(command=tipo.yview)
            tipo.place(x=100, y=100)
            #cantidad
            cedit_label = Label(ventana_estock2, text="Cantidad:")
            cedit_label.place(x=20, y=250)
            cedit = Entry(ventana_estock2)
            cedit.insert(END, data[2])
            cedit.pack()
            cedit.place(x=100, y=250)  
            #cxunidad
            cxuedit_label = Label(ventana_estock2, text="Costo por unidad ($):")
            cxuedit_label.place(x=20, y=300)
            cxuedit = Entry(ventana_estock2)
            cxuedit.insert(END, data[3])
            cxuedit.pack()
            cxuedit.place(x=150, y=300)  
            # Costototal
            costo2_label = Label(ventana_estock2, text="Costo por cantidad:")
            costo2_label.place(x=20, y=350)
            costo3_label = Label(ventana_estock2, text="0")
            costo3_label.place(x=200, y=350)
             #precioavender
            precio_a_vender_label = Label(ventana_estock2, text="Precio de venta ($):")
            precio_a_vender_label.place(x=20, y=400)
            precio_a_vender = Entry(ventana_estock2)
            precio_a_vender.insert(END, data[4])
            # Posicionarla en la ventana.
            precio_a_vender.place(x=150, y=400)
            ##Boton AÑADIR
            photoa = PhotoImage(file="img/edit_icon.png")  
            btn=Button(ventana_estock2, text="Editar", fg='green', command=añadir_a_la_base, image=photoa,compound=LEFT)
            btn.place(x=30, y=500)
            #Boton calcular
            photoc = PhotoImage(file="img/calc_icon.png")  
            btn=Button(ventana_estock2, text="Calcular costo por cantidad", command=auto, image=photoc,compound=LEFT)
            btn.place(x=160, y=500)
            ##Boton salir
            photoe = PhotoImage(file="img/exit_icon.png")  
            btn=Button(ventana_estock2, text="Salir", fg='red', command=ventana_estock2.destroy, image=photoe,compound=LEFT)
            btn.place(x=360, y=500)
            ventana_estock2.title('Editar stock') #Titulo de la ventana principal
            ventana_estock2.geometry("450x550") #Altura y anchura
            ventana_estock2['bg'] = '#833AB4'
            ventana_estock2.mainloop()
            return False
    ventana_estock = tk.Toplevel()
    ventana_estock.grab_set()
    ventana_estock.focus_set
    banners3 = PhotoImage(file="img/banner_stock.png")
    banners4 = banners3.subsample(3,2)
    titulo=Label(ventana_estock,image=banners4,compound=LEFT)
    titulo.place(x=60, y=10)
    #Obtener db
    db = "root.db"
    conn = conectar_con_la_db(db)
    cursor = conn.cursor()
    cursor.execute("SELECT producto FROM stock order by id")
    data=cursor.fetchall()
    producto_label = Label(ventana_estock, text="Seleccione el producto:")
    producto_label.place(x=20, y=100)
    scrollbar = Scrollbar(ventana_estock)
    scrollbar.pack(side=RIGHT, fill=Y)
    producto = Listbox(ventana_estock)
    producto.pack()
    for data in data:
        producto.insert(END, data)
    producto.config(yscrollcommand=scrollbar.set, height=5, selectmode=SINGLE, width=20)
    scrollbar.config(command=producto.yview)
    producto.place(x=150, y=100)
    ##Boton AÑADIR
    photoa = PhotoImage(file="img/edit_icon.png")  
    btn=Button(ventana_estock, text="Editar", fg='blue', command=estock2, image=photoa,compound=LEFT)
    btn.place(x=30, y=350)
    ##Boton salir
    photoe = PhotoImage(file="img/exit_icon.png")  
    btn=Button(ventana_estock, text="Salir", command=ventana_estock.destroy, image=photoe,compound=LEFT)
    btn.place(x=300, y=350)
    ventana_estock.title('Editar stock') #Titulo de la ventana principal
    ventana_estock.geometry("400x400") #Altura y anchura
    ventana_estock['bg'] = '#833AB4'
    ventana_estock.mainloop()
    return False