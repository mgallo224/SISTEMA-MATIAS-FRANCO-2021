from tkinter import *
import tkinter as tk
from etc.funciones_varias import llamar_a_buscarv,llamar_a_trending,llamar_a_calc
print("MODULO ACTIVO: {}" .format(__name__))

def admventas():
        if __name__ == "modulos.admventas":
                ventana_admventas = tk.Toplevel()
                ventana_admventas.grab_set()
                ventana_admventas.focus_set
                photo = PhotoImage(file = r"img\search_icon.png")
                btn=Button(ventana_admventas, text="Buscador de ventas",width=200 , height=30, image = photo,compound = LEFT, command=llamar_a_buscarv)       
                btn.place(x=80, y=100)
                banner = PhotoImage(file = r"img\banner_ventas.png")
                banner1 =  banner.subsample(3, 2)
                lbl=Label(ventana_admventas,image=banner1,compound=LEFT)
                lbl.place(x=60, y=10)
                photo1 = PhotoImage(file = r"img\calc_icon.png")  
                btn=Button(ventana_admventas, text="Calculadora de gastos", width=200 , height=30,image=photo1,compound=LEFT,command=llamar_a_calc)
                btn.place(x=80, y=150)
                photo3 = PhotoImage(file = r"img\trending_icon.png")  
                btn=Button(ventana_admventas, text="Productos mas vendidos",width=200 , height=30,image=photo3,compound=LEFT,command=llamar_a_trending)
                btn.place(x=80, y=200)
                photo4 = PhotoImage(file = r"img\exit_icon.png")  
                btn=Button(ventana_admventas, text="Salir", fg="red",width=200 , height=30, command=ventana_admventas.destroy,image=photo4,compound=LEFT)
                btn.place(x=80, y=300)
                ventana_admventas.title('Ventas') #Titulo de la ventana principal
                ventana_admventas.geometry("400x550") #Altura y anchura
                ventana_admventas['bg'] = '#db3236'
                ventana_admventas.mainloop() #Ejecución
        return False
