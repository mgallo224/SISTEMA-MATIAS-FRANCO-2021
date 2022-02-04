from tkinter import ttk
import tkinter as tk
from etc.funciones_varias import conectar_con_la_db
print("MODULO ACTIVO: {}" .format(__name__))
def vservicios():
    if __name__ == "modulos.submodulos.vservicios":
        def View():
            db = "root.db"
            conn = conectar_con_la_db(db)
            cursor = conn.cursor()
            cursor.execute("SELECT nombre,tipo,gxmes FROM servicios")
            rows = cursor.fetchall()    
            for row in rows:
                print(row) 
                tree.insert("", tk.END, values=row)        
            conn.close()
        ventana_vservicios = tk.Toplevel()
        ventana_vservicios.grab_set()
        ventana_vservicios.focus_set
        tree = ttk.Treeview(ventana_vservicios, column=("c1", "c2", "c3"), show='headings')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="Detalle")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="Tipo")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="Gasto por mes ($)")
        tree.pack()
        View()
        button1 = tk.Button(ventana_vservicios,text="Volver", command=ventana_vservicios.destroy)
        button1.pack(pady=10)
        ventana_vservicios.title("Lista de servicios")
        ventana_vservicios['bg'] = '#49A'
        ventana_vservicios.mainloop()