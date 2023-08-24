import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from controllers.productos import getProductos
from controllers.clientes import getClientes
from controllers.facturas import *

class NuevaFacturaForm(tk.Frame):
    def __init__(self, master, userSession):
        super().__init__(master)
        self.master = master
        self.userSession = userSession
        self.master.title("Factura")

        self.fecha = tk.StringVar()
        self.cliente = tk.StringVar()
        self.producto = tk.StringVar()
        self.cantidad = tk.IntVar()
        self.total = tk.DoubleVar()

        self.clientes = self.fillClientes()
        self.productos = self.fillProductos()
        
        self.crear_vista()
        self.delete_this_product = None

    def fillClientes(self):
        clientes = getClientes()
        nombres_clientes = []
        for c in clientes:
            nombres_clientes.append(c['nombres'])
        return nombres_clientes

    def fillProductos(self):
        products = getProductos()
        nombres_productos = []
        for c in products:
            nombres_productos.append(c['nombre'])
        return nombres_productos
    
    def crear_vista(self):
        tk.Label(self, text="Fecha:").grid(row=0, column=0, sticky="e")
        DateEntry(self, textvariable=self.fecha, date_pattern="dd/mm/y").grid(row=0, column=1, padx=(10,20))

        tk.Label(self, text=" ", height=1).grid(row=1)

        tk.Label(self, text="Cliente:").grid(row=2, column=0, sticky="e")
        tk.OptionMenu(self, self.cliente, *self.clientes).grid(row=2, column=1)

        tk.Label(self, text=" ", height=1).grid(row=3)

        tk.Label(self, text="Producto:").grid(row=4, column=0, sticky="e")
        tk.OptionMenu(self, self.producto, *self.productos).grid(row=4, column=1)

        tk.Label(self, text=" ", height=1).grid(row=5)

        tk.Label(self, text="Cantidad:").grid(row=6, column=0, sticky="e")
        tk.Entry(self, textvariable=self.cantidad).grid(row=6, column=1, padx=(10,20))

        tk.Label(self, text=" ", height=1).grid(row=7)

        tk.Button(self, text="Agregar", command=self.agregar).grid(row=8, column=1)
        tk.Button(self, text="Guardar", command=self.guardar).grid(row=8, column=2)
        tk.Button(self, text="Eliminar", command=self.eliminar).grid(row=8, column=3)
        tk.Button(self, text="Limpiar", command=self.limpiar).grid(row=8, column=4)

        tk.Label(self, text=" ", height=1).grid(row=9)

        self.tabla = ttk.Treeview(self, columns=("ID Producto", "Descripción", "Precio", "Cantidad", "Valor"), show="headings")
        self.tabla.heading("#1", text="Id Producto")
        self.tabla.heading("#2", text="Descripción")
        self.tabla.heading("#3", text="Precio")
        self.tabla.heading("#4", text="Cantidad")
        self.tabla.heading("#5", text="Valor")
        self.tabla.column("#1", width=80, anchor="center")
        self.tabla.column("#2", width=120, anchor="center")
        self.tabla.column("#3", width=80, anchor="center")
        self.tabla.column("#4", width=80, anchor="center")
        self.tabla.column("#5", width=150, anchor="center")
        self.tabla.grid(row=10, columnspan=5)

        self.tabla.bind("<ButtonRelease-1>", self.buscar)

        self.total_label = tk.Label(self, text="Total:")
        self.total_label.grid(row=12, column=3, sticky="e")

        # Evento para buscar usuario en la tabla
        self.tabla.bind("<ButtonRelease-1>", self.buscar)
    
    def agregar(self):
        producto = self.producto.get()
        cantidad = self.cantidad.get()
        productos = getProductos()

        for p in productos:
            if p['nombre'] == producto:
                row = (p['id'], p['nombre'], p['precio'], cantidad, float(p['precio']) * int(cantidad))
                self.tabla.insert("", "end", values=row)
                self.updateTotal()


    def buscar(self, event):
        item = self.tabla.selection()[0]
        self.delete_this_product = item
            
        
    def eliminar(self):
        if self.delete_this_product is not None:
             for item in self.tabla.get_children():
                if item == self.delete_this_product:
                    self.tabla.delete(item)
                    self.updateTotal()

    def limpiar(self):
        self.fecha.set("")
        self.cliente.set("")
        self.producto.set("")
        self.cantidad.set("")
        self.tabla.delete(*self.tabla.get_children())

    def guardar(self):
        fecha = self.fecha.get()
        cliente = self.cliente.get()

        data_table = []
        for item in self.tabla.get_children():
            values = self.tabla.item(item, "values")
            if values:
                data_table.append([values[1], values[3]]) 
        total = 0
        for item in self.tabla.get_children():
            values = self.tabla.item(item, "values")
            total += float(values[4])
        res = createFactura(fecha, cliente, data_table, total)
        clave = list(res.keys())[0]
        valor = res[clave]
        messagebox.showinfo(clave, valor)
        self.limpiar()

    def updateTotal(self):
        total = 0
        for item in self.tabla.get_children():
            values = self.tabla.item(item, "values")
            total += float(values[4])
        self.total_label.config(text=f"Total: {total}")