from tkinter import * #Importar tkinter
from etc.funciones_varias import llamar_a_cventas,llamar_a_admventas,llamar_a_admstock,llamar_a_admusers,llamar_a_admservicios #Importar las funciones dentro del modulo funci
print("MODULO Activo: {}" .format(__name__))

if __name__ == "modulos.principal":
        ventana_principal=Tk()
        banner = PhotoImage(file = r"img\banner.png")
        banner1 =  banner.subsample(3, 2)
        lbl=Label(ventana_principal,image=banner1,compound=LEFT)
        lbl.place(x=60, y=10)
        photo1 = PhotoImage(file = r"img\sale_icon.png")  
        btn=Button(ventana_principal, text="Cargar pedido", fg='#3cba54',  width=100 , height=30, image=photo1,compound=LEFT, command=llamar_a_cventas)
        btn.place(x=80, y=100)
        photo2 = PhotoImage(file = r"img\adm_icon.png")  
        btn=Button(ventana_principal, text="Ventas", fg="#db3236", width=100 , height=30, image=photo2,compound=LEFT,command=llamar_a_admventas)
        btn.place(x=80, y=150)
        photo3 = PhotoImage(file = r"img\vendor_icon.png")  
        btn=Button(ventana_principal, text="Stock", width=100 , height=30,fg="#833AB4", image=photo3,compound=LEFT, command=llamar_a_admstock)
        btn.place(x=80, y=200)
        photo8 = PhotoImage(file = r"img\user_icon.png")  
        btn=Button(ventana_principal, text="Empleados", fg="#f4c20d", width=100 , height=30,image=photo8,compound=LEFT, command=llamar_a_admusers)
        btn.place(x=80, y=250)
        photose = PhotoImage(file = r"img\services_icon.png")  
        btn=Button(ventana_principal, text="Servicios", fg="#49A", width=100 , height=30,image=photose,compound=LEFT, command=llamar_a_admservicios)
        btn.place(x=80, y=300)
        photo4 = PhotoImage(file = r"img\exit_icon.png")  
        btn=Button(ventana_principal, text="Salir",  width=100 , height=30, command=ventana_principal.destroy,image=photo4,compound=LEFT)
        btn.place(x=80, y=400)
        ventana_principal.title('Casa de comidas "Delivery"') #Titulo de la ventana principal
        ventana_principal['bg'] = '#4285F4'
        ventana_principal.geometry("300x450") #Altura y anchura
        ventana_principal.mainloop() #Ejecución
