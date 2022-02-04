from tkinter import *
from tkinter import messagebox
import tkinter as tk
from etc.funciones_varias import conectar_con_la_db,fechayhora
print("MODULO ACTIVO: {}" .format(__name__))


def aservicios():
    def añadir_a_la_base():
        db = "root.db"
        conn = conectar_con_la_db(db)
        cursor = conn.cursor()
        obproducto0 = producto.get()
        obproducto = obproducto0.capitalize()
        obgasto = gasto.get()
        obtipo = tipo.get(ACTIVE)
        fecha = fechayhora()
        if len(obproducto)<=1 or len(obgasto)<=0 or len(obtipo)<=0:
            return messagebox.showerror('Error', 'Valores no validos, ingrese nuevamente los valores')
        elif  obgasto.isnumeric() == False:
            return messagebox.showerror('Error', 'El gasto debe ser numerico')
        elif  int(obgasto)<=0:
            return messagebox.showerror('Error', 'El gasto debe ser mayor a 0')
        else:
                cursor.execute("select nombre from servicios where nombre=? and tipo=?",(obproducto,obtipo,))
                data = cursor.fetchone()
                if (data is None) == False:
                    return messagebox.showerror("Error", "El servicio ya se encuentra agregado")
                else:
                    cursor.execute("insert into servicios (nombre,tipo,gxmes,fecha) values (?, ?, ?,?)",(obproducto,obtipo,obgasto,fecha))
                    conn.commit()
                    cursor.close()
                    messagebox.showinfo('Añadido', 'El servicio '+obproducto+' fue añadido correctamente')
                    return producto.delete(0,END),gasto.delete(0,END),tipo.selection_clear(0, tk.END)
    if __name__ == "modulos.submodulos.aservicios":
        ventana_aservicios = tk.Toplevel()
        ventana_aservicios.grab_set()
        ventana_aservicios.focus_set
        banners3 = PhotoImage(file="img/banner_servicios.png")
        banners4 = banners3.subsample(3,2)
        titulo=Label(ventana_aservicios,image=banners4,compound=LEFT)
        titulo.place(x=60, y=10)
        # Crear caja de texto cantidad
        producto_label = Label(ventana_aservicios, text="Detalles:")
        producto_label.place(x=20, y=200)
        producto = tk.Entry(ventana_aservicios)
        # Posicionarla en la ventana.
        producto.place(x=100, y=200)
        # Crear caja de texto tipo
        tipor=["Luz","Gas","Agua","Internet","Impuestos","Proveedores","Varios"]
        tipo_label = Label(ventana_aservicios, text="Tipo:")
        tipo_label.place(x=20, y=100)
        scrollbar = Scrollbar(ventana_aservicios)
        scrollbar.pack(side=RIGHT, fill=Y)
        tipo = Listbox(ventana_aservicios)
        tipo.pack()
        for tipor in tipor:
            tipo.insert(END, tipor)
        tipo.config(yscrollcommand=scrollbar.set, height=5, selectmode=SINGLE, width=20)
        scrollbar.config(command=tipo.yview)
        tipo.place(x=100, y=100)
        # Crear caja de texto gxmes
        gasto_label = Label(ventana_aservicios, text="Gasto ($):")
        gasto_label.place(x=20, y=250)
        gasto = tk.Entry(ventana_aservicios)
        # Posicionarla en la ventana.
        gasto.place(x=100, y=250)
        ##Boton AÑADIR
        photoa = PhotoImage(file="img/save_icon.png")  
        btn=Button(ventana_aservicios, text="Agregar servicio", fg='green', command=añadir_a_la_base, image=photoa,compound=LEFT)
        btn.place(x=30, y=350)
        ##Boton salir
        photoe = PhotoImage(file="img/exit_icon.png")  
        btn=Button(ventana_aservicios, text="Salir", fg='red', command=ventana_aservicios.destroy, image=photoe,compound=LEFT)
        btn.place(x=200, y=350)
        ventana_aservicios.title('Agregar servicio') #Titulo de la ventana principal
        ventana_aservicios.geometry("300x400") #Altura y anchura
        ventana_aservicios['bg'] = '#49A'
        ventana_aservicios.mainloop()
    return False
