from tkinter import *
import tkinter as tk
from etc.funciones_varias import llamar_a_estock,llamar_a_astock,llamar_a_dstock,llamar_a_vstock
def admstock():
    if __name__ == "modulos.admstock":
        ventana_admstock = tk.Toplevel()
        ventana_admstock.grab_set()
        ventana_admstock.focus_set
        ventana_admstock.geometry("300x400")
        banner = PhotoImage(file = r"img\banner_stock.png")
        banner1 =  banner.subsample(3, 2)
        lbl=Label(ventana_admstock,image=banner1,compound=LEFT)
        lbl.place(x=60, y=10)
        photo9 = PhotoImage(file = r"img\store_icon.png")
        btn=Button(ventana_admstock, text="Ver stock", image = photo9,compound = LEFT,  width=100 , height=30, command=llamar_a_vstock)        
        btn.place(x=80, y=100)
        photo = PhotoImage(file = r"img\stock_icon.png")
        btn=Button(ventana_admstock, text="Alta stock", fg='green',  width=100 , height=30, image = photo,compound = LEFT, command=llamar_a_astock)        
        btn.place(x=80, y=150)
        photo6 = PhotoImage(file = r"img\edit_icon.png")
        btn=Button(ventana_admstock, text="Editar stock", fg='blue',  width=100 , height=30, image = photo6,compound = LEFT, command=llamar_a_estock)        
        btn.place(x=80, y=200)
        photo5 = PhotoImage(file = r"img\delete2_icon.png")
        btn=Button(ventana_admstock, text="Baja stock", fg='red',  width=100 , height=30, image = photo5,compound = LEFT, command=llamar_a_dstock)        
        btn.place(x=80, y=250)
        photo4 = PhotoImage(file = r"img\exit_icon.png")  
        btn=Button(ventana_admstock, text="Salir", fg='red',  width=100 , height=30, command=ventana_admstock.destroy,image=photo4,compound=LEFT)
        btn.place(x=80, y=350)
        ventana_admstock.title("Stock")
        ventana_admstock['bg'] = '#833AB4'
        ventana_admstock.mainloop()