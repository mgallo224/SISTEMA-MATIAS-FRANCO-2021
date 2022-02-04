from tkinter import *
from tkinter import messagebox
import tkinter as tk
from etc.funciones_varias import conectar_con_la_db
print("MODULO ACTIVO: {}" .format(__name__))

######################COMIENZO BUSCAR X PRODUCTO##################################################################

def buscarvxp():
    def buscarvxp2():
        db = "root.db"
        conn = conectar_con_la_db(db)
        cursor = conn.cursor()
        obtener_producto0 = producto.get(ACTIVE)
        obtener_producto = obtener_producto0[0] 
        cursor.execute("SELECT producto,fecha,precio,cantidad,ncliente,dcliente,liquidacion,tipo,mes FROM ventas WHERE producto = ? ORDER BY fecha DESC", (obtener_producto,))
        data=cursor.fetchall()
        conn.commit()
        cursor.close()
        if len(data)==0:
            return messagebox.showerror('Oops!', 'El producto ingresado aun no fue vendido')
        else:
            return buscarvxp3(data)

    def buscarvxp3(data):
        from tkinter import ttk
        def View():
            rows = data   
            for row in rows:
                print(row) 
                tree.insert("", tk.END, values=row)        
            conn.close()

        ventana_buscarv2 = tk.Toplevel()
        ventana_buscarv2.grab_set()
        ventana_buscarv2.focus_set
        tree = ttk.Treeview(ventana_buscarv2, column=("c1", "c2", "c3","c4","c5","c6","c7","c8","c9"), show='headings')
        tree.column("#1", anchor=tk.CENTER, width=150)
        tree.heading("#1", text="Producto vendido")
        tree.column("#2", anchor=tk.CENTER, width=120)
        tree.heading("#2", text="Fecha de la venta")
        tree.column("#3", anchor=tk.CENTER, width=120)
        tree.heading("#3", text="Precio vendido ($)")
        tree.column("#4", anchor=tk.CENTER, width=120)
        tree.heading("#4", text="Cantidades vendidas")
        tree.column("#5", anchor=tk.CENTER, width=160)
        tree.heading("#5", text="Nombre del cliente")
        tree.column("#6", anchor=tk.CENTER, width=160)
        tree.heading("#6", text="Dirección del cliente")
        tree.column("#7", anchor=tk.CENTER, width=120)
        tree.heading("#7", text="Ganancia neta ($)")
        tree.column("#8", anchor=tk.CENTER, width=160)
        tree.heading("#8", text="Tipo")
        tree.column("#9", anchor=tk.CENTER, width=120)
        tree.heading("#9", text="Mes")
        tree.pack()
        View()
        button1 = tk.Button(ventana_buscarv2,text="Volver", command=ventana_buscarv2.destroy)
        button1.pack(pady=10)
        ventana_buscarv2['bg'] = '#db3236'
        ventana_buscarv2.title("Buscar venta por producto")
        ventana_buscarv2.mainloop()
        return False


    if __name__ == "modulos.submodulos.buscarv":
        ventana_buscarv = tk.Toplevel()
        ventana_buscarv.grab_set()
        ventana_buscarv.focus_set
        banners3 = PhotoImage(file="img/banner_ventas.png")
        banners4 = banners3.subsample(3,2)
        titulo=Label(ventana_buscarv,image=banners4,compound=LEFT)
        titulo.place(x=60, y=10)
        #Crear lista producto#
        #Obtener db
        db = "root.db"
        conn = conectar_con_la_db(db)
        cursor = conn.cursor()
        cursor.execute("SELECT producto FROM stock order by id")
        data=cursor.fetchall()
        producto_label = Label(ventana_buscarv, text="Seleccione el producto:")
        producto_label.place(x=20, y=100)
        scrollbar = Scrollbar(ventana_buscarv)
        scrollbar.pack(side=RIGHT, fill=Y)
        producto = Listbox(ventana_buscarv)
        producto.pack()
        for data in data:
            print(data)
            producto.insert(END, data)
        producto.config(yscrollcommand=scrollbar.set, height=5, selectmode=SINGLE, width=20)
        scrollbar.config(command=producto.yview)
        producto.place(x=150, y=100)
        ##Boton buscqar
        photoa = PhotoImage(file="img/search_icon.png")  
        btn=Button(ventana_buscarv, text="Buscar", fg='green', command=buscarvxp2, image=photoa,compound=LEFT)
        btn.place(x=20, y=500)
        ##Boton salir
        photoe = PhotoImage(file="img/exit_icon.png")  
        btn=Button(ventana_buscarv, text="Salir", fg='red', command=ventana_buscarv.destroy, image=photoe,compound=LEFT)
        btn.place(x=200, y=500)
        ventana_buscarv.title('Buscar ventas por producto') #Titulo de la ventana principal
        ventana_buscarv.geometry("300x550") #Altura y anchura
        ventana_buscarv['bg'] = '#db3236'
        ventana_buscarv.mainloop()
    return False


######################FIN BUSCAR X PRODUCTO##################################################################

######################COMIENZO BUSCAR X TIPO##################################################################


def buscarvxt():
    def buscarvxt2():
        db = "root.db"
        conn = conectar_con_la_db(db)
        cursor = conn.cursor()
        obtipo = tipo.get(ACTIVE)
        cursor.execute("SELECT producto,fecha,precio,cantidad,ncliente,dcliente,liquidacion,tipo,mes FROM ventas WHERE tipo = ? ORDER BY fecha DESC", (obtipo,))
        data=cursor.fetchall()
        conn.commit()
        cursor.close()
        if len(data)==0:
            return messagebox.showerror('Oops!', 'El tipo ingresado aun no fue vendido')
        else:
            return buscarvxt3(data,conn)

    def buscarvxt3(data,conn):
        from tkinter import ttk
        def View():
            rows = data   
            for row in rows:
                print(row) 
                tree.insert("", tk.END, values=row)        
            conn.close()

        ventana_buscarv2 = tk.Toplevel()
        ventana_buscarv2.grab_set()
        ventana_buscarv2.focus_set
        tree = ttk.Treeview(ventana_buscarv2, column=("c1", "c2", "c3","c4","c5","c6","c7","c8","c9"), show='headings')
        tree.column("#1", anchor=tk.CENTER, width=150)
        tree.heading("#1", text="Producto vendido")
        tree.column("#2", anchor=tk.CENTER, width=120)
        tree.heading("#2", text="Fecha de la venta")
        tree.column("#3", anchor=tk.CENTER, width=120)
        tree.heading("#3", text="Precio vendido ($)")
        tree.column("#4", anchor=tk.CENTER, width=120)
        tree.heading("#4", text="Cantidades vendidas")
        tree.column("#5", anchor=tk.CENTER, width=160)
        tree.heading("#5", text="Nombre del cliente")
        tree.column("#6", anchor=tk.CENTER, width=160)
        tree.heading("#6", text="Dirección del cliente")
        tree.column("#7", anchor=tk.CENTER, width=120)
        tree.heading("#7", text="Ganancia neta ($)")
        tree.column("#8", anchor=tk.CENTER, width=160)
        tree.heading("#8", text="Tipo")
        tree.column("#9", anchor=tk.CENTER, width=120)
        tree.heading("#9", text="Mes")
        tree.pack()
        View()
        button1 = tk.Button(ventana_buscarv2,text="Volver", command=ventana_buscarv2.destroy)
        button1.pack(pady=10)
        ventana_buscarv2['bg'] = '#db3236'
        ventana_buscarv2.title("Buscar venta por tipo")
        ventana_buscarv2.mainloop()
        return False


    if __name__ == "modulos.submodulos.buscarv":
        ventana_buscarvt = tk.Toplevel()
        ventana_buscarvt.grab_set()
        ventana_buscarvt.focus_set
        banners3 = PhotoImage(file="img/banner_ventas.png")
        banners4 = banners3.subsample(3,2)
        titulo=Label(ventana_buscarvt,image=banners4,compound=LEFT)
        titulo.place(x=60, y=10)
        #Crear lista producto#
        #Obtener db
        tipor=["Bebida","Postre","Guarnición","Entrada","Pizzas","Empanadas","Pastas"]
        tipo_label = Label(ventana_buscarvt, text="Tipo:")
        tipo_label.place(x=20, y=100)
        scrollbar = Scrollbar(ventana_buscarvt)
        scrollbar.pack(side=RIGHT, fill=Y)
        tipo = Listbox(ventana_buscarvt)
        tipo.pack()
        for tipor in tipor:
            tipo.insert(END, tipor)
        tipo.config(yscrollcommand=scrollbar.set, height=5, selectmode=SINGLE, width=20)
        scrollbar.config(command=tipo.yview)
        tipo.place(x=100, y=100)
        ##Boton buscqar
        photoa = PhotoImage(file="img/search_icon.png")  
        btn=Button(ventana_buscarvt, text="Buscar", fg='green', command=buscarvxt2, image=photoa,compound=LEFT)
        btn.place(x=20, y=500)
        ##Boton salir
        photoe = PhotoImage(file="img/exit_icon.png")  
        btn=Button(ventana_buscarvt, text="Salir", fg='red', command=ventana_buscarvt.destroy, image=photoe,compound=LEFT)
        btn.place(x=200, y=500)
        ventana_buscarvt.title('Buscar ventas por tipo') #Titulo de la ventana principal
        ventana_buscarvt.geometry("300x550") #Altura y anchura
        ventana_buscarvt['bg'] = '#db3236'
        ventana_buscarvt.mainloop()
    return False


######################FIN BUSCAR X TIPO##################################################################

######################COMIENZO BUSCAR X fecha##################################################################


def buscarvxf():
    def buscarvxf2():
        db = "root.db"
        conn = conectar_con_la_db(db)
        cursor = conn.cursor()
        obmes0 = fechar.curselection()
        obmes = int(obmes0[0])+1
        cursor.execute("SELECT producto,fecha,precio,cantidad,ncliente,dcliente,liquidacion,tipo,mes FROM ventas WHERE mes = ? ORDER BY fecha DESC", (obmes,))
        data=cursor.fetchall()
        conn.commit()
        cursor.close()
        if len(data)==0:
            return messagebox.showerror('Oops!', 'No hay ventas en este mes')
        else:
            return buscarvxf3(data,conn)

    def buscarvxf3(data,conn):
        from tkinter import ttk
        def View():
            rows = data   
            for row in rows:
                print(row) 
                tree.insert("", tk.END, values=row)        
            conn.close()

        ventana_buscarv2 = tk.Toplevel()
        ventana_buscarv2.grab_set()
        ventana_buscarv2.focus_set
        tree = ttk.Treeview(ventana_buscarv2, column=("c1", "c2", "c3","c4","c5","c6","c7","c8","c9"), show='headings')
        tree.column("#1", anchor=tk.CENTER, width=150)
        tree.heading("#1", text="Producto vendido")
        tree.column("#2", anchor=tk.CENTER, width=120)
        tree.heading("#2", text="Fecha de la venta")
        tree.column("#3", anchor=tk.CENTER, width=120)
        tree.heading("#3", text="Precio vendido ($)")
        tree.column("#4", anchor=tk.CENTER, width=120)
        tree.heading("#4", text="Cantidades vendidas")
        tree.column("#5", anchor=tk.CENTER, width=160)
        tree.heading("#5", text="Nombre del cliente")
        tree.column("#6", anchor=tk.CENTER, width=160)
        tree.heading("#6", text="Dirección del cliente")
        tree.column("#7", anchor=tk.CENTER, width=120)
        tree.heading("#7", text="Ganancia neta ($)")
        tree.column("#8", anchor=tk.CENTER, width=160)
        tree.heading("#8", text="Tipo")
        tree.column("#9", anchor=tk.CENTER, width=120)
        tree.heading("#9", text="Mes")
        tree.pack()
        View()
        button1 = tk.Button(ventana_buscarv2,text="Volver", command=ventana_buscarv2.destroy)
        button1.pack(pady=10)
        ventana_buscarv2['bg'] = '#db3236'
        ventana_buscarv2.title("Buscar venta por mes")
        ventana_buscarv2.mainloop()
        return False


    if __name__ == "modulos.submodulos.buscarv":
        ventana_buscarvf = tk.Toplevel()
        ventana_buscarvf.grab_set()
        ventana_buscarvf.focus_set
        banners3 = PhotoImage(file="img/banner_ventas.png")
        banners4 = banners3.subsample(3,2)
        titulo=Label(ventana_buscarvf,image=banners4,compound=LEFT)
        titulo.place(x=60, y=10)
        #Crear lista producto#
        #Obtener db
        fechalista=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
        fechar_label = Label(ventana_buscarvf, text="Mes:")
        fechar_label.place(x=20, y=100)
        scrollbar = Scrollbar(ventana_buscarvf)
        scrollbar.pack(side=RIGHT, fill=Y)
        fechar = Listbox(ventana_buscarvf)
        fechar.pack()
        for fechalista in fechalista:
            fechar.insert(END, fechalista)
        fechar.config(yscrollcommand=scrollbar.set, height=5, selectmode=SINGLE, width=20)
        scrollbar.config(command=fechar.yview)
        fechar.place(x=100, y=100)
        ##Boton buscqar
        photoa = PhotoImage(file="img/search_icon.png")  
        btn=Button(ventana_buscarvf, text="Buscar", fg='green', command=buscarvxf2, image=photoa,compound=LEFT)
        btn.place(x=20, y=500)
        ##Boton salir
        photoe = PhotoImage(file="img/exit_icon.png")  
        btn=Button(ventana_buscarvf, text="Salir", fg='red', command=ventana_buscarvf.destroy, image=photoe,compound=LEFT)
        btn.place(x=200, y=500)
        ventana_buscarvf.title('Buscar ventas por mes') #Titulo de la ventana principal
        ventana_buscarvf.geometry("300x550") #Altura y anchura
        ventana_buscarvf['bg'] = '#db3236'
        ventana_buscarvf.mainloop()
    return False


######################FIN BUSCAR X fecha##################################################################



##############################VENTANA BUSQUEDA PRINCIPAl#############################################################

def buscarv():
        if __name__ == "modulos.submodulos.buscarv":
                ventana_admventas = tk.Toplevel()
                ventana_admventas.grab_set()
                ventana_admventas.focus_set
                photo = PhotoImage(file = r"img\search2_icon.png")
                btn=Button(ventana_admventas, text="Buscar por producto",width=200 , height=30, image = photo,compound = LEFT, command=buscarvxp)       
                btn.place(x=80, y=100)
                banner = PhotoImage(file = r"img\banner_ventas.png")
                banner1 =  banner.subsample(3, 2)
                lbl=Label(ventana_admventas,image=banner1,compound=LEFT)
                lbl.place(x=60, y=10)
                photo1 = PhotoImage(file = r"img\search2_icon.png")  
                btn=Button(ventana_admventas, text="Buscar por tipo", width=200 , height=30,image=photo1,compound=LEFT,command=buscarvxt)
                btn.place(x=80, y=150)
                photo3 = PhotoImage(file = r"img\search2_icon.png")  
                btn=Button(ventana_admventas, text="Buscar por mes",width=200 , height=30,image=photo3,compound=LEFT, command=buscarvxf)
                btn.place(x=80, y=200)
                photo4 = PhotoImage(file = r"img\exit_icon.png")  
                btn=Button(ventana_admventas, text="Salir", fg="red",width=200 , height=30, command=ventana_admventas.destroy,image=photo4,compound=LEFT)
                btn.place(x=80, y=300)
                ventana_admventas.title('Buscador de ventas') #Titulo de la ventana principal
                ventana_admventas.geometry("400x550") #Altura y anchura
                ventana_admventas['bg'] = '#db3236'
                ventana_admventas.mainloop() #Ejecución
        return False