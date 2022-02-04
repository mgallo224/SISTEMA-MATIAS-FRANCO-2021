from tkinter import *
import tkinter as tk
from etc.funciones_varias import llamar_a_eusers,llamar_a_dusers,llamar_a_vusers,llamar_a_addusers
def admusers():
    if __name__ == "modulos.admusers":
        ventana_admusers = tk.Toplevel()
        ventana_admusers.grab_set()
        ventana_admusers.focus_set
        ventana_admusers.geometry("300x400")
        banner = PhotoImage(file = r"img\banner_u.png")
        banner1 =  banner.subsample(3, 2)
        lbl=Label(ventana_admusers,image=banner1,compound=LEFT)
        lbl.place(x=60, y=10)
        photo9 = PhotoImage(file = r"img\user2_icon.png")
        btn=Button(ventana_admusers, text="Ver empleados", width=150 , height=30,  image = photo9,compound = LEFT, command=llamar_a_vusers)        
        btn.place(x=80, y=100)
        photo = PhotoImage(file = r"img\usersadd_icon.png")
        btn=Button(ventana_admusers, text="Alta empleados", fg='green', width=150 , height=30,  image = photo,compound = LEFT, command=llamar_a_addusers)        
        btn.place(x=80, y=150)
        photo6 = PhotoImage(file = r"img\edit_icon.png")
        btn=Button(ventana_admusers, text="Editar empleados", fg='blue', width=150 , height=30,  image = photo6,compound = LEFT, command=llamar_a_eusers)        
        btn.place(x=80, y=200)
        photo5 = PhotoImage(file = r"img\usersremove_icon.png")
        btn=Button(ventana_admusers, text="Baja empleados", fg='red', width=150 , height=30,  image = photo5,compound = LEFT, command=llamar_a_dusers)        
        btn.place(x=80, y=250)
        photo4 = PhotoImage(file = r"img\exit_icon.png")  
        btn=Button(ventana_admusers, text="Salir", fg='red', width=150 , height=30,  command=ventana_admusers.destroy,image=photo4,compound=LEFT)
        btn.place(x=80, y=350)
        ventana_admusers.title("Empleados")
        ventana_admusers['bg'] = '#f4c20d'
        ventana_admusers.mainloop()