import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tkinter as tk
from etc.funciones_varias import conectar_con_la_db,fechayhora,mes,año
print("MODULO ACTIVO: {}" .format(__name__))
def cventas():
    def auto():
            if not producto.curselection() or len(cantidad.get()) == 0 or cantidad.get().isnumeric() == False:
                precio2_label['text'] = "0"
            else:
                prod =  producto.curselection()
                prod1 = int(prod[0])+1
                cursor.execute("SELECT producto FROM stock WHERE id = ?", (prod1,))
                data1 = cursor.fetchone()
                cursor.execute("SELECT precioventa from stock where producto=?", (data1[0],))
                data2 = cursor.fetchone()
                precio2_label['text'] = int(cantidad.get())*int(data2[0])
            precio2_label.after(2000, auto)  


    def añadir_a_la_base():
        db = "root.db"
        conn = conectar_con_la_db(db)
        cursor = conn.cursor()
        obtener_producto0 =  producto.curselection()
        obtener_cantidad = cantidad.get()
        obtener_nombreyapellidocliente0 = nombreyapellidocliente.get()
        obtener_nombreyapellidocliente = obtener_nombreyapellidocliente0.capitalize()
        obtener_direccioncliente0 = direccioncliente.get()
        obtener_direccioncliente = obtener_direccioncliente0.capitalize()
        parallevar0 = ventana_cventas.checkbox_value.get()
        parallevar = int(parallevar0)
        checkmulti0 = multi_value.get()
        checkmulti = int(checkmulti0)
        fecha = fechayhora()
        obmes = mes()
        obaño = año()
        if not obtener_producto0:
            return messagebox.showerror("Error", "Debe seleccionar un producto")
        elif obtener_cantidad.isnumeric() == False:
            return messagebox.showerror('Error', 'El precio y cantidad deben ser numericos')
        elif len(obtener_cantidad)<=0:
            return messagebox.showerror('Error', 'Valores no validos, ingrese nuevamente los valores')
        elif int(obtener_cantidad)<=0:
            return messagebox.showerror('Error', 'El precio y cantidad deben mayores a 0')
        elif obtener_nombreyapellidocliente.isnumeric() == True:
            return messagebox.showerror("Error","El nombre no es valido")
        else:
            obtener_producto = int(obtener_producto0[0])+1
            cursor.execute("SELECT cantidad,tipo,producto FROM stock WHERE id = ?", (obtener_producto,))
            data0=cursor.fetchone()
            cursor.execute("SELECT precioventa from stock where producto=?", (data0[2],))
            precio = cursor.fetchone()
            obtener_precio = int(obtener_cantidad)*int(precio[0])
            if data0[0]<int(obtener_cantidad):
                return messagebox.showerror('Error', 'La cantidad ingresada del producto excede al stock del mismo')
            if parallevar == 1 and (len(obtener_direccioncliente)<=0 or len(obtener_nombreyapellidocliente)<=0):
                    messagebox.showerror('Error', 'Si es para llevar debes indicar el nombre y dirección del cliente')
            else:
                cursor.execute("SELECT costoxunidad from stock where producto=?",(data0[2],))
                costoxun = cursor.fetchone()
                liquidacion = int(obtener_precio)-int(costoxun[0])*int(obtener_cantidad)
                cursor.execute("insert into carrito (producto,cantidad,precio,fecha,ncliente,dcliente,parallevar,mes,año,tipo,liquidacion) values (?, ?, ?, ?, ?, ?,?,?,?,?,?)",(data0[2], obtener_cantidad, obtener_precio,fecha, obtener_nombreyapellidocliente, obtener_direccioncliente,parallevar,obmes,obaño,data0[1],liquidacion))
                conn.commit()
                cursor.close()
                if checkmulti == 0:
                    return messagebox.showinfo("Añadido al carrito", "El pedido fue cargado al carrito de compra"), cantidad.delete(0,END),nombreyapellidocliente.delete(0,END),direccioncliente.delete(0,END),ventana_cventas.checkbox_value.set(0),producto.selection_clear(0, tk.END)
                else:
                    return messagebox.showinfo("Añadido al carrito", "El pedido fue cargado al carrito de compra"), cantidad.delete(0,END),producto.selection_clear(0, tk.END)


    if __name__ == "modulos.cventas":
        ventana_cventas = tk.Toplevel()
        ventana_cventas.grab_set()
        ventana_cventas.focus_set
        banners3 = PhotoImage(file="img/banner_cp.png")
        banners4 = banners3.subsample(3,2)
        titulo=Label(ventana_cventas,image=banners4,compound=LEFT)
        titulo.place(x=60, y=10)
        #Crear lista producto#
        #Obtener db
        db = "root.db"
        conn = conectar_con_la_db(db)
        cursor = conn.cursor()
        cursor.execute("SELECT producto,tipo FROM stock order by id")
        data=cursor.fetchall()
        producto_label = Label(ventana_cventas, text="Pedido:")
        producto_label.place(x=20, y=300)
        scrollbar = Scrollbar(ventana_cventas)
        scrollbar.pack(side=RIGHT, fill=Y)
        producto = Listbox(ventana_cventas)
        producto.pack()
        for data in data:
            lista = list(data)
            producto.insert(END, lista[0]+"-"+lista[1])
        producto.config(yscrollcommand=scrollbar.set, height=5, selectmode=SINGLE, width=50)
        scrollbar.config(command=producto.yview)
        producto.place(x=150, y=300)
        #ingresar otro pedido para el cliente
        multi_value = tk.BooleanVar(ventana_cventas)
        multi = ttk.Checkbutton(ventana_cventas, text="Agregar otro pedido al mismo cliente", variable=multi_value)
        multi.place(x=200, y=400)
        # Crear caja de texto cantidad
        cantidad_label = Label(ventana_cventas, text="Ingrese la cantidad:")
        cantidad_label.place(x=20, y=100)
        cantidad = tk.Entry(ventana_cventas)
        # Posicionarla en la ventana.
        cantidad.place(x=150, y=100)
        # Crear caja de texto precio
        precio_label = Label(ventana_cventas, text="Precio:")
        precio_label.place(x=20, y=150)
        precio2_label = Label(ventana_cventas, text="0")
        precio2_label.place(x=200, y=150)
        auto()
        # Crear caja de texto nombre cliente
        nombreyapellidocliente_label = Label(ventana_cventas, text="Nombre y apellido del cliente (Opcional):")
        nombreyapellidocliente_label.place(x=20, y=200)
        nombreyapellidocliente = tk.Entry(ventana_cventas)
        # Posicionarla en la ventana.
        nombreyapellidocliente.place(x=250, y=200)
        # Crear caja de texto direccion cliente
        direccioncliente_label = Label(ventana_cventas, text="Dirección del cliente (Opcional):")
        direccioncliente_label.place(x=20, y=250)
        direccioncliente = tk.Entry(ventana_cventas)
        # Posicionarla en la ventana.
        direccioncliente.place(x=200, y=250)
        #checkbox delivery
        ventana_cventas.checkbox_value = tk.BooleanVar(ventana_cventas)
        ventana_cventas.checkbox = ttk.Checkbutton(ventana_cventas, text="Para llevar", variable=ventana_cventas.checkbox_value)
        ventana_cventas.checkbox.place(x=20, y=400)
        ##Boton AÑADIR
        photoa = PhotoImage(file="img/adds_icon.png")  
        btn=Button(ventana_cventas, text="Añadir al carrito", fg='green',  width=130 , height=30, command=añadir_a_la_base, image=photoa,compound=LEFT)
        btn.place(x=30, y=500)
        ##Boton ver
        photover = PhotoImage(file="img/shopping_icon.png")  
        btn=Button(ventana_cventas, text="Ver carrito", fg='blue',  width=100 , height=30, command=vercarrito, image=photover,compound=LEFT)
        btn.place(x=200, y=500)
        ##Boton salir
        photoe = PhotoImage(file="img/exit_icon.png")  
        btn=Button(ventana_cventas, text="Salir", fg='red',  width=100 , height=30, command=ventana_cventas.destroy, image=photoe,compound=LEFT)
        btn.place(x=350, y=500)
        ventana_cventas.title('Cargar pedido') #Titulo de la ventana principal
        ventana_cventas.geometry("550x550") #Altura y anchura
        ventana_cventas['bg'] = '#3cba54'
        ventana_cventas.mainloop()
    return False


def vercarrito():
        def pdf(obtener_producto,obtener_cantidad,obtener_precio,fecha,obmes,obaño):
            rand = random.randint(1,9999)
            cvas = canvas.Canvas("facturas/"+str(rand)+"_"+str(obmes)+"-"+str(obaño)+".pdf", pagesize=letter)
            cvas.setLineWidth(.3)
            cvas.setFont('Helvetica', 11)
            cvas.drawString(30,750,'Casa de comidas "Delivery"')
            cvas.drawString(30,735,fecha)
            cvas.drawString(500,750,"Cantidad:"+str(obtener_cantidad))
            cvas.line(480,747,580,747)
            cvas.drawString(205,725,"Pedido:")
            cvas.drawString(300,725,obtener_producto)
            cvas.drawString(30,703,'Precio:')
            cvas.line(120,700,580,700)
            cvas.drawString(120,703,"$"+str(obtener_precio))
            cvas.save() 
            return messagebox.showinfo("Carga exitosa", "El pedido fue cargado exitosamente, se genero en la carpeta del programa la factura de nombre: "+str(rand)+"_"+str(obmes)+"-"+str(obaño)+".pdf")
            
        def añadir():
            db = "root.db"
            conn = conectar_con_la_db(db)
            cursor = conn.cursor()
            cursor.execute("select producto,cantidad,precio,fecha,mes,año,id from carrito")
            infopdf = cursor.fetchall()
            cursor.execute("select MAX(id) from carrito")
            rango = cursor.fetchone()
            lista_productos = []
            if all(elem is None for elem in infopdf) == True:
                conn.commit()
                cursor.close()
                return messagebox.showerror('Oops!', 'El carrito esta vacio')
            else:
                for i in range(rango[0]):
                    lista_productos.append(infopdf[i][0])
                    print(lista_productos)
                    pdfproducto = "/".join(lista_productos)
                    cursor.execute("SELECT cantidad,tipo,producto FROM stock WHERE producto = ?", (infopdf[i][0],))
                    data0=cursor.fetchone()
                    cantidad_a_restar = data0[0]-int(infopdf[i][1])
                    cursor.execute("UPDATE stock SET cantidad=? where producto=?", (cantidad_a_restar,data0[2]))
                    cursor.execute("SELECT veces,vxunidad,cantidad FROM stock WHERE producto = ?", (data0[2],))
                    veces=cursor.fetchone()
                    cursor.execute("SELECT SUM(cantidad) from carrito where producto = ?", (infopdf[i][0],))
                    correccion = cursor.fetchone()
                    if veces[2]+1<int(correccion[0]):
                        conn.commit
                        cursor.close()
                        return messagebox.showerror("Oops", "Parece que la suma de la cantidad de un producto en la lista excede el stock del mismo, no se puede continuar con la compra")
                    vxunidad = veces[1]+int(infopdf[i][1])
                    cursor.execute("UPDATE stock SET veces=?, vxunidad=? where producto=?", (veces[0]+1,vxunidad, data0[2]))
                cursor.execute("SELECT SUM(cantidad),SUM(precio) from carrito") 
                suma = cursor.fetchone() 
                pdf(pdfproducto,suma[0],suma[1],infopdf[i][3],infopdf[i][4],infopdf[i][5])
                cursor.execute("INSERT INTO ventas(producto,cantidad,precio,fecha,ncliente,dcliente,parallevar,mes,año,tipo,liquidacion) SELECT producto,cantidad,precio,fecha,ncliente,dcliente,parallevar,mes,año,tipo,liquidacion FROM carrito;")
                cursor.execute("DELETE FROM carrito")
                conn.commit()
                cursor.close()
                return ventana_cventas2.destroy()

        def eraseall():
            db = "root.db"
            conn = conectar_con_la_db(db)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM carrito")
            erase = cursor.fetchall()
            print(erase)
            if len(erase)==0:
                return messagebox.showerror("Error", "El carrito ya esta vacio")
            else:
                cursor.execute("DELETE FROM carrito")
                conn.commit()
                cursor.close()
                messagebox.showinfo('Eliminado', 'El carrito fue eliminado correctamente')
                return ventana_cventas2.destroy()

        def view():
                db = "root.db"
                conn = conectar_con_la_db(db)
                cursor = conn.cursor()
                cursor.execute("SELECT producto,cantidad,precio,ncliente,dcliente FROM carrito")
                rows = cursor.fetchall()    
                for row in rows:
                    print(row) 
                    tree.insert("", tk.END, values=row)        
                conn.close()

        ventana_cventas2 = tk.Toplevel()
        ventana_cventas2.grab_set()
        ventana_cventas2.focus_set
        tree = ttk.Treeview(ventana_cventas2, column=("c1", "c2", "c3","c4","c5"), show='headings')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="Producto")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="Cantidad")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="Precio ($)")
        tree.column("#4", anchor=tk.CENTER)
        tree.heading("#4", text="Nombre del cliente")
        tree.column("#5", anchor=tk.CENTER)
        tree.heading("#5", text="Dirección")
        tree.pack()
        view()
        db = "root.db"
        conn = conectar_con_la_db(db)
        cursor = conn.cursor()
        cursor.execute("select SUM(precio), SUM(cantidad) from carrito")
        i = cursor.fetchone()
        if all(elem is None for elem in i) ==  False:
            info1 = "Precio total del carrito: $"+str(i[0])
            p_label = Label(ventana_cventas2, text=info1)
            p_label.pack(pady=10)
            info2 = "Cantidad total del carrito: "+str(i[1])
            p_label = Label(ventana_cventas2, text=info2)
            p_label.pack(pady=10)
        button1 = tk.Button(ventana_cventas2,text="Cargar venta", command=añadir)
        button1.pack(pady=10)
        button2 = tk.Button(ventana_cventas2,text="Eliminar carrito",command=eraseall)
        button2.pack(pady=10)
        button3 = tk.Button(ventana_cventas2,text="Salir", command=ventana_cventas2.destroy)
        button3.pack(pady=10)
        ventana_cventas2.title("Ver carrito")
        ventana_cventas2['bg'] = '#3cba54'
        ventana_cventas2.mainloop()
        return False