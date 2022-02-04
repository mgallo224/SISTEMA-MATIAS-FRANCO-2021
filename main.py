from tkinter import * 
from etc.funciones_varias import crear_db,checkaño,crear_directorio
print("MODULO Activo: {}" .format(__name__))
if __name__ =='__main__':
    crear_db()
    checkaño()
    crear_directorio("facturas")
    import modulos.principal