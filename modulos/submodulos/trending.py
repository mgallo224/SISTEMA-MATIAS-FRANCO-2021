from tkinter import ttk
import tkinter as tk
from etc.funciones_varias import conectar_con_la_db
print("MODULO ACTIVO: {}" .format(__name__))
def trending():
    if __name__ == "modulos.submodulos.trending":
        def View():
            db = "root.db"
            conn = conectar_con_la_db(db)
            cursor = conn.cursor()
            cursor.execute("SELECT producto,veces,vxunidad FROM stock order by veces DESC")
            rows = cursor.fetchall()    
            for row in rows:
                print(row) 
                tree.insert("", tk.END, values=row)        
            conn.close()

        ventana_trending = tk.Toplevel()
        ventana_trending.grab_set()
        ventana_trending.focus_set
        tree = ttk.Treeview(ventana_trending, column=("c1", "c2","c3"), show='headings')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="Nombre")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="Numero de veces vendido")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="Cantidades vendidas")
        tree.pack()
        View()
        button1 = tk.Button(ventana_trending,text="Volver", command=ventana_trending.destroy)
        button1.pack(pady=10)
        ventana_trending['bg'] = '#db3236'
        ventana_trending.title("Productos mas vendidos")
        ventana_trending.mainloop()