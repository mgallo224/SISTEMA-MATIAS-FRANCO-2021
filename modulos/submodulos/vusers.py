from tkinter import ttk
import tkinter as tk
from etc.funciones_varias import conectar_con_la_db
print("MODULO ACTIVO: {}" .format(__name__))
def vusers():
    if __name__ == "modulos.submodulos.vusers":
        def View():
            db = "root.db"
            conn = conectar_con_la_db(db)
            cursor = conn.cursor()
            cursor.execute("SELECT dni,nombre,apellido,jerarquia,legajo,sueldo,fecha FROM empleados order by legajo DESC")
            rows = cursor.fetchall()    
            for row in rows:
                print(row) 
                tree.insert("", tk.END, values=row)        
            conn.close()
        ventana_vusers = tk.Toplevel()
        ventana_vusers.grab_set()
        ventana_vusers.focus_set
        tree = ttk.Treeview(ventana_vusers, column=("c1", "c2", "c3","c4","c5","c6","c7"), show='headings')
        tree.column("#1", anchor=tk.CENTER, width=80)
        tree.heading("#1", text="Dni")
        tree.column("#2", anchor=tk.CENTER, width=120)
        tree.heading("#2", text="Nombre")
        tree.column("#3", anchor=tk.CENTER, width=120)
        tree.heading("#3", text="Apellido")
        tree.column("#4", anchor=tk.CENTER, width=100)
        tree.heading("#4", text="Cargo")
        tree.column("#5", anchor=tk.CENTER, width=60)
        tree.heading("#5", text="Legajo")
        tree.column("#6", anchor=tk.CENTER, width=100)
        tree.heading("#6", text="Sueldo ($)")
        tree.column("#7", anchor=tk.CENTER, width=120)
        tree.heading("#7", text="Ingreso")
        tree.pack()
        View()
        button1 = tk.Button(ventana_vusers,text="Volver", command=ventana_vusers.destroy)
        button1.pack(pady=10)
        ventana_vusers.title("Lista de empleados")
        ventana_vusers['bg'] = '#f4c20d'
        ventana_vusers.mainloop()
