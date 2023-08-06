import tkinter as tk
from Ayuda import *
from Cambio_Clave import *
from Cambio_Usuario import *
from Clientes import *
from Nueva_Factura import *
from Productos import *
from Reporte_Facturas import *
from Usuarios import *

root = tk.Tk()
root.geometry("400x200")
root.title("SISTEMA DE FACTURACIÓN")

menu_principal = tk.Menu()

menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_movimientos = tk.Menu(menu_principal, tearoff=0)
menu_ayuda = tk.Menu(menu_principal, tearoff=0)

menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_principal.add_cascade(label="Movimientos", menu=menu_movimientos)
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)

menu_archivo.add_command(label="Usuarios", command=FormUsuarios)
menu_archivo.add_command(label="Clientes", command=FormClientes)
menu_archivo.add_command(label="Productos", command=FormProductos)
menu_archivo.add_separator()
menu_archivo.add_command(label="Cambio Clave", command=FormCambioClave)
menu_archivo.add_command(label="Cambio Usuario", command=FormCambioUsuario)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)

menu_movimientos.add_command(label="Nueva Factura", command=FormNuevaFactura)
menu_movimientos.add_command(label="Reporte Facturas", command=FormReporteFacturas)

menu_ayuda.add_command(label="Acerca de", command=FormAyuda)

root.config(menu=menu_principal)

root.mainloop()