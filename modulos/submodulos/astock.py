from tkinter import *
from tkinter import messagebox
import tkinter as tk
from etc.funciones_varias import conectar_con_la_db,fechayhora
print("MODULO ACTIVO: {}" .format(__name__))


def astock():

    def auto():
        if len(cantidad.get()) == 0 or len(costo.get()) == 0 or cantidad.get().isnumeric() == False or costo.get().isnumeric() == False:
            costo3_label['text'] = "0"
        else:
            costo3_label['text'] = int(cantidad.get())*int(costo.get())
        ventana_cstock.after(2000, auto)  
        return False
    def añadir_a_la_base():
        db = "root.db"
        conn = conectar_con_la_db(db)
        cursor = conn.cursor()
        obproducto0 = producto.get()
        obproducto = obproducto0.capitalize()
        obcantidad = cantidad.get()
        obcostoxunidad = costo.get()
        obprecioventa = precio_a_vender.get()
        obtipo = tipo.get(ACTIVE)
        fecha = fechayhora()
        cxcant = int(cantidad.get())*int(costo.get())
        if len(obproducto)<=1 or len(obcantidad)<=0 or len(obtipo)<=0 or len(obcostoxunidad)<=0 or len(obprecioventa)<=0:
            return messagebox.showerror('Error', 'Valores no validos, ingrese nuevamente los valores')
        elif  obcantidad.isnumeric() == False or obcostoxunidad.isnumeric() == False or obprecioventa.isnumeric() == False:
            return messagebox.showerror('Error', 'La cantidad,el costo y el precio deben ser numericos')
        elif  int(obcantidad)<=0 or int(obcostoxunidad)<=0 or int(cxcant)<=0 or int(obprecioventa)<=0:
            return messagebox.showerror('Error', 'La cantidad,el costo y el precio deben ser mayores a 0')
        else:
                cursor.execute("select producto from stock where producto=?",(obproducto,))
                data = cursor.fetchone()
                if (data is None) == False:
                    return messagebox.showerror("Error", "El producto ya existe en el stock,para editarlo ingrese al modulo editar stock")
                else:
                    cursor.execute("insert into stock (producto,tipo,cantidad,fecha,veces,vxunidad,costoxunidad,costoxcantidad,precioventa) values (?, ?, ?, ?,?,?,?,?,?)",(obproducto,obtipo,obcantidad,fecha,0,0,obcostoxunidad,cxcant,obprecioventa))
                    conn.commit()
                    cursor.close()
                    messagebox.showinfo('Añadido', 'El producto '+obproducto+' fue añadido correctamente al stock')
                    return producto.delete(0,END),cantidad.delete(0,END),costo.delete(0,END),tipo.selection_clear(0, tk.END),precio_a_vender.delete(0,END)

    if __name__ == "modulos.submodulos.astock":
        ventana_cstock = tk.Toplevel()
        ventana_cstock.grab_set()
        ventana_cstock.focus_set
        banners3 = PhotoImage(file="img/banner_stock.png")
        banners4 = banners3.subsample(3,2)
        titulo=Label(ventana_cstock,image=banners4,compound=LEFT)
        titulo.place(x=60, y=10)
        # Crear caja de texto cantidad
        producto_label = Label(ventana_cstock, text="Detalles:")
        producto_label.place(x=20, y=200)
        producto = tk.Entry(ventana_cstock)
        # Posicionarla en la ventana.
        producto.place(x=100, y=200)
        # tipo
        tipor=["Bebida","Postre","Guarnición","Entrada","Pizzas","Empanadas","Pastas"]
        tipo_label = Label(ventana_cstock, text="Tipo:")
        tipo_label.place(x=20, y=100)
        scrollbar = Scrollbar(ventana_cstock)
        scrollbar.pack(side=RIGHT, fill=Y)
        tipo = Listbox(ventana_cstock)
        tipo.pack()
        for tipor in tipor:
            tipo.insert(END, tipor)
        tipo.config(yscrollcommand=scrollbar.set, height=5, selectmode=SINGLE, width=20)
        scrollbar.config(command=tipo.yview)
        tipo.place(x=100, y=100)
        # Cantidad
        cantidad_label = Label(ventana_cstock, text="Cantidad:")
        cantidad_label.place(x=20, y=250)
        cantidad = tk.Entry(ventana_cstock)
        # Posicionarla en la ventana.
        cantidad.place(x=100, y=250)
        # Cxu
        costo_label = Label(ventana_cstock, text="Costo por unidad ($):")
        costo_label.place(x=20, y=300)
        costo = tk.Entry(ventana_cstock)
        # Posicionarla en la ventana.
        costo.place(x=150, y=300)
        # Costototal
        costo2_label = Label(ventana_cstock, text="Costo por cantidad ($):")
        costo2_label.place(x=20, y=350)
        costo3_label = Label(ventana_cstock, text="0")
        costo3_label.place(x=200, y=350)
        #precioavender
        precio_a_vender_label = Label(ventana_cstock, text="Precio de venta ($):")
        precio_a_vender_label.place(x=20, y=400)
        precio_a_vender = tk.Entry(ventana_cstock)
        # Posicionarla en la ventana.
        precio_a_vender.place(x=150, y=400)
        ##Boton AÑADIR
        photoa = PhotoImage(file="img/save_icon.png")  
        btn=Button(ventana_cstock, text="Agregar al stock", fg='green', command=añadir_a_la_base, image=photoa,compound=LEFT)
        btn.place(x=30, y=500)
        #Boton calcular
        photoc = PhotoImage(file="img/calc_icon.png")  
        btn=Button(ventana_cstock, text="Calcular costo por cantidad", command=auto, image=photoc,compound=LEFT)
        btn.place(x=160, y=500)
        ##Boton salir
        photoe = PhotoImage(file="img/exit_icon.png")  
        btn=Button(ventana_cstock, text="Salir", fg='red', command=ventana_cstock.destroy, image=photoe,compound=LEFT)
        btn.place(x=360, y=500)
        ventana_cstock.title('Agregar stock') #Titulo de la ventana principal
        ventana_cstock.geometry("450x550") #Altura y anchura
        ventana_cstock['bg'] = '#833AB4'
        ventana_cstock.mainloop()
    return False