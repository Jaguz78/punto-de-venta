import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from controllers.productos import getProductos
from controllers.clientes import getClientes
from controllers.facturas import *
from utils import *
from validaciones.v_nuevafactura import *

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
            nombres_clientes.append(c[2])
        return nombres_clientes

    def fillProductos(self):
        products = getProductos()
        nombres_productos = []
        for c in products:
            nombres_productos.append(c[1])
        return nombres_productos
    
    def crear_vista(self):
        tk.Label(self, text="Fecha:").grid(row=0, column=0, sticky="e", pady=10)
        DateEntry(self, textvariable=self.fecha, date_pattern="dd/mm/y").grid(row=0, column=1, padx=(10,20), pady=10)

        tk.Label(self, text="Cliente:").grid(row=1, column=0, sticky="e", pady=10)
        tk.OptionMenu(self, self.cliente, *self.clientes).grid(row=1, column=1, pady=10)

        tk.Label(self, text="Producto:").grid(row=2, column=0, sticky="e", pady=10)
        tk.OptionMenu(self, self.producto, *self.productos).grid(row=2, column=1, pady=10)

        tk.Label(self, text="Cantidad:").grid(row=3, column=0, sticky="e", pady=10)
        tk.Entry(self, textvariable=self.cantidad).grid(row=3, column=1, padx=(10,20), pady=10)

        tk.Button(self, text="Agregar", command=self.agregar).grid(row=4, column=1, pady=10)
        tk.Button(self, text="Guardar", command=self.guardar).grid(row=4, column=2, pady=10)
        tk.Button(self, text="Eliminar", command=self.eliminar).grid(row=4, column=3, pady=10)
        tk.Button(self, text="Limpiar", command=self.limpiar).grid(row=4, column=4, pady=10)

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
        self.tabla.grid(row=5, columnspan=5, pady=10)

        self.tabla.bind("<ButtonRelease-1>", self.buscar)

        self.total_label = tk.Label(self, text="Total:")
        self.total_label.grid(row=6, column=3, sticky="e", pady=10)

        self.tabla.bind("<ButtonRelease-1>", self.buscar)

        tk.Button(self, text="<-", command=lambda: retroceder(self.tabla), width=5, pady=10).grid(row=7, column=1, pady=20)
        tk.Button(self, text="<<-", command=lambda: retrocederTodo(self.tabla), width=5, pady=10).grid(row=7, column=2, pady=20)
        tk.Button(self, text="->>", command=lambda: avanzarTodo(self.tabla), width=5, pady=10).grid(row=7, column=3, pady=20)
        tk.Button(self, text="->", command=lambda: avanzar(self.tabla), width=5, pady=10).grid(row=7, column=4, pady=20)
    
    def agregar(self):
        producto = self.producto.get()
        cantidad = self.cantidad.get()
        productos = getProductos()
        if v_enagregarp(producto, cantidad):
            for p in productos:
                if p[1] == producto:
                    row = (p[0], p[1], p[2], cantidad, float(p[2]) * int(cantidad))
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
        self.total_label.config(text="Total:")

    def guardar(self):
        fecha = self.fecha.get()
        cliente = self.cliente.get()
        if v_enguardar(fecha, cliente):
            data_table = []
            for item in self.tabla.get_children():
                values = self.tabla.item(item, "values")
                if values:
                    data_table.append([values[0], values[3], values[4]]) 
            total = 0
            for item in self.tabla.get_children():
                values = self.tabla.item(item, "values")
                total += float(values[4])
            createFactura(fecha, cliente, self.userSession.username, data_table, total)
            self.limpiar()

    def updateTotal(self):
        total = 0
        for item in self.tabla.get_children():
            values = self.tabla.item(item, "values")
            total += float(values[4])
        self.total_label.config(text=f"Total: {total}")