from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tkinter as tk
import random
from etc.funciones_varias import conectar_con_la_db,fechayhora,mes,año
print("MODULO ACTIVO: {}" .format(__name__))
def cventas():
    def auto():
            if not producto.curselection() or len(cantidad.get()) == 0 or cantidad.get().isnumeric() == False:
                precio2_label['text'] = "0"
            else:
                prod =  producto.curselection()
                listamultiple = []
                for prod in prod:    
                    cursor.execute("SELECT producto FROM stock WHERE id = ?", (prod+1,))
                    data1 = cursor.fetchone()
                    cursor.execute("SELECT precioventa from stock where producto=?", (data1[0],))
                    data2 = cursor.fetchone()
                    listamultiple.append(int(cantidad.get())*int(data2[0]))
                    print(listamultiple)
                    precio2_label['text'] = sum(listamultiple)
            precio2_label.after(2000, auto)  


    def pdf(obtener_producto,obtener_cantidad,obtener_precio,fecha,obmes,obaño):
        rand = random.randint(1,999)
        cvas = canvas.Canvas("facturas/"+str(obtener_producto)+"_"+str(obmes)+"-"+str(obaño)+"___"+str(rand)+".pdf", pagesize=letter)
        cvas.setLineWidth(.3)
        cvas.setFont('Helvetica', 11)
        cvas.drawString(30,750,'Casa de comidas "Delivery"')
        cvas.drawString(30,735,fecha)
        cvas.drawString(500,750,"Cantidad:"+obtener_cantidad)
        cvas.line(480,747,580,747)
        cvas.drawString(275,725,"Pedido:")
        cvas.drawString(500,725,obtener_producto)
        cvas.line(378,723,580,723)
        cvas.drawString(30,703,'Precio:')
        cvas.line(120,700,580,700)
        cvas.drawString(120,703,"$"+str(obtener_precio))
        cvas.save() 
        return messagebox.showinfo("Carga exitosa", "El pedido fue cargado exitosamente, se genero en la carpeta del programa la factura de nombre: "+str(obtener_producto)+"_"+str(obmes)+"-"+str(obaño)+"___"+str(rand)+".pdf")
        
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
        
            if parallevar == 1 and (len(obtener_direccioncliente)<=0 or len(obtener_nombreyapellidocliente)<=0):
                    messagebox.showerror('Error', 'Si es para llevar debes indicar el nombre y dirección del cliente')
            else:
                for obtener_producto0 in obtener_producto0:
                    cursor.execute("SELECT cantidad,tipo,producto FROM stock WHERE id = ?", (obtener_producto0+1,))
                    data0=cursor.fetchone()
                    cursor.execute("SELECT precioventa from stock where producto=?", (data0[2],))
                    precio = cursor.fetchone()
                    obtener_precio = int(obtener_cantidad)*int(precio[0])
                    cursor.execute("SELECT costoxunidad from stock where producto=?",(data0[2],))
                    costoxun = cursor.fetchone()
                    liquidacion = int(obtener_precio)-int(costoxun[0])*int(obtener_cantidad)
                    cursor.execute("SELECT cantidad,tipo,producto FROM stock WHERE id = ?", (obtener_producto0+1,))
                    data0=cursor.fetchone()
                    cursor.execute("insert into ventas (producto,cantidad,precio,fecha,ncliente,dcliente,parallevar,mes,año,tipo,liquidacion) values (?, ?, ?, ?, ?, ?,?,?,?,?,?)",(data0[2], obtener_cantidad, obtener_precio,fecha, obtener_nombreyapellidocliente, obtener_direccioncliente,parallevar,obmes,obaño,data0[1],liquidacion))
                    cantidad_a_restar = data0[0]-int(obtener_cantidad)
                    cursor.execute("UPDATE stock SET cantidad=? where producto=?", (cantidad_a_restar,data0[2]))
                    cursor.execute("SELECT veces,vxunidad FROM stock WHERE producto = ?", (data0[2],))
                    veces=cursor.fetchone()
                    vxunidad = veces[1]+int(obtener_cantidad)
                    cursor.execute("UPDATE stock SET veces=?, vxunidad=? where producto=?", (veces[0]+1,vxunidad, data0[2]))
                    conn.commit()
                    pdf(data0[2],obtener_cantidad,obtener_precio,fecha,obmes,obaño)
                cursor.close()    
                return cantidad.delete(0,END),nombreyapellidocliente.delete(0,END),direccioncliente.delete(0,END),ventana_cventas.checkbox_value.set(0),producto.selection_clear(0, tk.END)

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
        producto.config(yscrollcommand=scrollbar.set, height=5, selectmode=MULTIPLE, width=50)
        scrollbar.config(command=producto.yview)
        producto.place(x=150, y=300)
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
        photoa = PhotoImage(file="img/save_icon.png")  
        btn=Button(ventana_cventas, text="Cargar", fg='green',  width=100 , height=30, command=añadir_a_la_base, image=photoa,compound=LEFT)
        btn.place(x=30, y=500)
        ##Boton salir
        photoe = PhotoImage(file="img/exit_icon.png")  
        btn=Button(ventana_cventas, text="Salir", fg='red',  width=100 , height=30, command=ventana_cventas.destroy, image=photoe,compound=LEFT)
        btn.place(x=300, y=500)
        ventana_cventas.title('Cargar pedido') #Titulo de la ventana principal
        ventana_cventas.geometry("500x550") #Altura y anchura
        ventana_cventas['bg'] = '#3cba54'
        ventana_cventas.mainloop()
    return False

