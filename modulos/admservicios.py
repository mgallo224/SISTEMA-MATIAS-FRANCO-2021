from tkinter import *
import tkinter as tk
from etc.funciones_varias import llamar_a_aservicios,llamar_a_dservicios,llamar_a_vservicios
def admservicios():
    if __name__ == "modulos.admservicios":
        ventana_admservicios = tk.Toplevel()
        ventana_admservicios.grab_set()
        ventana_admservicios.focus_set
        ventana_admservicios.geometry("300x350")
        banner = PhotoImage(file = r"img\banner_servicios.png")
        banner1 =  banner.subsample(3, 2)
        lbl=Label(ventana_admservicios,image=banner1,compound=LEFT)
        lbl.place(x=60, y=10)
        photo9 = PhotoImage(file = r"img\views_icon.png")
        btn=Button(ventana_admservicios, text="Ver servicios", width=100 , height=30, image = photo9,compound = LEFT, command=llamar_a_vservicios)        
        btn.place(x=80, y=100)
        photo = PhotoImage(file = r"img\adds_icon.png")
        btn=Button(ventana_admservicios, text="Alta servicio", width=100 , height=30, fg='green', image = photo,compound = LEFT, command=llamar_a_aservicios)        
        btn.place(x=80, y=150)
        photo5 = PhotoImage(file = r"img\removes_icon.png")
        btn=Button(ventana_admservicios, text="Baja servicio", width=100 , height=30, fg='red', image = photo5,compound = LEFT, command=llamar_a_dservicios)        
        btn.place(x=80, y=200)
        photo4 = PhotoImage(file = r"img\exit_icon.png")  
        btn=Button(ventana_admservicios, text="Salir", width=100 , height=30, fg='red', command=ventana_admservicios.destroy,image=photo4,compound=LEFT)
        btn.place(x=80, y=300)
        ventana_admservicios['bg'] = '#49A'
        ventana_admservicios.title("Servicios")
        ventana_admservicios.mainloop()