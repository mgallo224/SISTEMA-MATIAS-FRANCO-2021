from tkinter import Message, ttk
import tkinter as tk
from etc.funciones_varias import conectar_con_la_db,mes
print("MODULO ACTIVO: {}" .format(__name__))
def calc():
    if __name__ == "modulos.submodulos.calc":
        def View():
            from tkinter import messagebox
            db = "root.db"
            conn = conectar_con_la_db(db)
            cursor = conn.cursor()
            meses = mes()
            print(meses)
            cursor.execute("SELECT SUM(precio), SUM(liquidacion) FROM ventas WHERE mes = ?", (meses,))
            ventasmes = cursor.fetchone()
            cursor.execute("SELECT sum(sueldo) from empleados")
            sueldos = cursor.fetchone()
            cursor.execute("SELECT sum(gxmes) from servicios")
            servicios = cursor.fetchone()
            if servicios[0]==None or sueldos[0]==None or ventasmes[0]==None or ventasmes[1]==None:
                    tree.insert("", tk.END) 
                    messagebox.showinfo('Ups!', "Para ver el calculo se tienen que cargar empleados,servicios y realizar una venta")
                    ventana_calc.destroy()
            else:
                ganancias = int(ventasmes[1])-int(sueldos[0])-int(servicios[0])
                rows = ["$"+str(ventasmes[0]), "$"+str(ventasmes[1]),"$"+str(sueldos[0]), "$"+str(servicios[0]),"$"+str(ganancias)]  
                tree.insert("", tk.END, values=rows)        
                conn.close()

        ventana_calc = tk.Toplevel()
        ventana_calc.grab_set()
        ventana_calc.focus_set
        tree = ttk.Treeview(ventana_calc, column=("c1", "c2", "c3","c4","c5"), show='headings')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="Ganancia bruta al mes")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="Ganancia a liquidar al mes")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="Gasto en sueldos")
        tree.column("#4", anchor=tk.CENTER)
        tree.heading("#4", text="Gasto en servicios")
        tree.column("#5", anchor=tk.CENTER)
        tree.heading("#5", text="Total mes")
        tree.pack()
        View()
        button1 = tk.Button(ventana_calc,text="Volver", command=ventana_calc.destroy)
        button1.pack(pady=10)
        ventana_calc['bg'] = '#db3236'
        ventana_calc.title("Calculadora de gastos")
        ventana_calc.mainloop()