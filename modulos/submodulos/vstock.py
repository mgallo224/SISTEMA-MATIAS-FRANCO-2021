from tkinter import ttk
import tkinter as tk
from etc.funciones_varias import conectar_con_la_db
print("MODULO ACTIVO: {}" .format(__name__))
def vstock():
    if __name__ == "modulos.submodulos.vstock":
        def View():
            db = "root.db"
            conn = conectar_con_la_db(db)
            cursor = conn.cursor()
            cursor.execute("SELECT producto,tipo,cantidad,costoxunidad,costoxcantidad,precioventa FROM stock")
            rows = cursor.fetchall()    
            for row in rows:
                print(row) 
                tree.insert("", tk.END, values=row)        
            conn.close()

        ventana_vstock = tk.Toplevel()
        ventana_vstock.grab_set()
        ventana_vstock.focus_set
        tree = ttk.Treeview(ventana_vstock, column=("c1", "c2", "c3","c4","c5","c6"), show='headings')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="Detalle")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="Tipo")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="Cantidad disponible")
        tree.column("#4", anchor=tk.CENTER)
        tree.heading("#4", text="Costo por unidad ($)")
        tree.column("#5", anchor=tk.CENTER)
        tree.heading("#5", text="Costo por cantidad ($)")
        tree.column("#6", anchor=tk.CENTER)
        tree.heading("#6", text="Precio de venta ($)")
        tree.pack()
        View()
        button1 = tk.Button(ventana_vstock,text="Volver", command=ventana_vstock.destroy)
        button1.pack(pady=10)
        ventana_vstock.title("Ver stock")
        ventana_vstock['bg'] = '#833AB4'
        ventana_vstock.mainloop()