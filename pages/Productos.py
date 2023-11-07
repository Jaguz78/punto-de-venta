import tkinter as tk
from tkinter import ttk
from controllers.productos import *
from tkinter import messagebox
from utils import *
from validaciones.v_productos import *

class ProductosForm(tk.Frame):
    def __init__(self, master, userSession):
        super().__init__(master)
        self.master = master
        self.userSession = userSession
        self.master.title("Gestión de Productos")

        self.id_producto = tk.StringVar() ###
        self.nombre = tk.StringVar()
        self.precio = tk.StringVar()
        self.iva = tk.StringVar()
        self.nota = tk.StringVar()
        
        self.ivas = self.fillIva()

        self.crear_vista()
    
    def fillIva(self):
        iva = getIva()
        porcentajes = []
        for i in iva:
            porcentajes.append(i[1])
        return porcentajes

    def crear_vista(self):
        tk.Label(self, text="Nombre:").grid(row=0, column=0, sticky="e", pady=10)
        tk.Entry(self, textvariable=self.nombre, width=30).grid(row=0, column=1, padx=(10,20), pady=10)

        tk.Label(self, text="Precio:").grid(row=0, column=2, sticky="e", pady=10)
        tk.Entry(self, textvariable=self.precio, width=30).grid(row=0, column=3, padx=(10,20), pady=10)

        tk.Label(self, text="Nota:").grid(row=1, column=0, sticky="e", pady=10)
        tk.Entry(self, textvariable=self.nota, width=30).grid(row=1, column=1, padx=(10,20), pady=10)

        tk.Label(self, text="IVA:").grid(row=1, column=2, sticky="e", pady=10)
        tk.OptionMenu(self, self.iva, *self.ivas).grid(row=1, column=3, padx=(10,20), pady=10)

        tk.Button(self, text="Agregar", command=self.agregar).grid(row=2, column=0, pady=10)
        tk.Button(self, text="Editar", command=self.editar).grid(row=2, column=1, pady=10)
        tk.Button(self, text="Eliminar", command=self.eliminar).grid(row=2, column=2, pady=10)
        tk.Button(self, text="Limpiar", command=self.limpiar).grid(row=2, column=3, pady=10)

        self.tabla = ttk.Treeview(self, columns=("Id Producto", "Nombre", "Precio", "IVA", "Nota"), show="headings")
        self.tabla.heading("#1", text="Id Producto")
        self.tabla.heading("#2", text="Nombre")
        self.tabla.heading("#3", text="Precio")
        self.tabla.heading("#4", text="IVA")
        self.tabla.heading("#5", text="Nota")
        self.tabla.column("#1", width=80, anchor="center")
        self.tabla.column("#2", width=120, anchor="center")
        self.tabla.column("#3", width=80, anchor="center")
        self.tabla.column("#4", width=80, anchor="center")
        self.tabla.column("#5", width=150, anchor="center")
        self.tabla.grid(row=3, columnspan=5, pady=10)

        self.setTable() 

        tk.Button(self, text="<-", command=lambda: retroceder(self.tabla), width=5, pady=10).grid(row=4, column=0, pady=20)
        tk.Button(self, text="<<-", command=lambda: retrocederTodo(self.tabla), width=5, pady=10).grid(row=4, column=1, pady=20)
        tk.Button(self, text="->>", command=lambda: avanzarTodo(self.tabla), width=5, pady=10).grid(row=4, column=2, pady=20)
        tk.Button(self, text="->", command=lambda: avanzar(self.tabla), width=5, pady=10).grid(row=4, column=3, pady=20)

        self.tabla.bind("<ButtonRelease-1>", self.buscar)
    
    def agregar(self):
        id = self.id_producto.get() ###
        nombre = self.nombre.get()
        precio = self.precio.get()
        iva = self.iva.get()
        nota = self.nota.get()
        if v_enguardar(nombre, precio, iva, nota):
            agregar_producto(nombre, precio, iva, nota)
            self.setTable()

    def buscar(self, event):
        item = self.tabla.selection()[0]
        values = self.tabla.item(item, "values")
        if values:
            self.id_producto.set(values[0])
            self.nombre.set(values[1])
            self.precio.set(values[2])
            self.iva.set(values[3])
            self.nota.set(values[4])

    def editar(self):
        id = self.id_producto.get() ###
        nombre = self.nombre.get()
        precio = self.precio.get()
        iva = self.iva.get()
        nota = self.nota.get()
        if v_eneditar(nombre, precio, iva, nota):
            editar_producto(id, nombre, precio, iva, nota)
            self.setTable()

    def eliminar(self):
        id = self.id_producto.get() ###
        if v_eneliminar(id):
            eliminar_producto(id)
            self.setTable()

    def limpiar(self):
        self.id_producto.set("") ###
        self.nombre.set("")
        self.precio.set("")
        self.iva.set("")
        self.nota.set("")

    def setTable(self):
        productos = getProductos()
        for p in self.tabla.get_children():
            self.tabla.delete(p)
        for p in productos:
            row = (p[0], p[1], p[2], p[3], p[4])
            self.tabla.insert("", "end", values=row)