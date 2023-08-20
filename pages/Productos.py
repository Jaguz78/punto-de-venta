import tkinter as tk
from tkinter import ttk
from controllers.productos import *
from tkinter import messagebox

class ProductosForm(tk.Frame):
    def __init__(self, master, userSession):
        super().__init__(master)
        self.master = master
        self.userSession = userSession
        self.master.title("Gestión de Productos")

        self.id_producto = tk.StringVar()
        self.nombre = tk.StringVar()
        self.precio = tk.StringVar()
        self.iva = tk.StringVar()
        self.nota = tk.StringVar()
        
        self.crear_vista()
    
    def crear_vista(self):
        tk.Label(self, text="Id Producto:").grid(row=0, column=0, sticky="e")
        tk.Entry(self, textvariable=self.id_producto, width=30).grid(row=0, column=1, padx=(10,20))

        tk.Label(self, text=" ", height=1).grid(row=1)

        tk.Label(self, text="Nombre:").grid(row=2, column=0, sticky="e")
        tk.Entry(self, textvariable=self.nombre, width=30).grid(row=2, column=1, padx=(10,20))

        tk.Label(self, text=" ", height=1).grid(row=3)

        tk.Label(self, text="Precio:").grid(row=4, column=0, sticky="e")
        tk.Entry(self, textvariable=self.precio, width=30).grid(row=4, column=1, padx=(10,20))

        tk.Label(self, text="IVA:").grid(row=4, column=2, sticky="e")
        tk.OptionMenu(self, self.iva, "5%", "12%").grid(row=4, column=3, padx=(10,20))

        tk.Label(self, text=" ", height=1).grid(row=5)

        tk.Label(self, text="Nota:").grid(row=6, column=0, sticky="e")
        tk.Entry(self, textvariable=self.nota, width=30).grid(row=6, column=1, padx=(10,20))

        tk.Label(self, text=" ", height=1).grid(row=7)

        tk.Button(self, text="Agregar", command=self.agregar).grid(row=8, column=0)
        tk.Button(self, text="Editar", command=self.editar).grid(row=8, column=1)
        tk.Button(self, text="Eliminar", command=self.eliminar).grid(row=8, column=2)
        tk.Button(self, text="Limpiar", command=self.limpiar).grid(row=8, column=3)

        tk.Label(self, text=" ", height=1).grid(row=9)

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
        self.tabla.grid(row=10, columnspan=5)

        self.setTable()

        self.tabla.bind("<ButtonRelease-1>", self.buscar)
    
    def agregar(self):
        id = self.id_producto.get()
        nombre = self.nombre.get()
        precio = self.precio.get()
        iva = self.iva.get()
        nota = self.nota.get()
        res = agregar_producto(id, nombre, precio, iva, nota)
        clave = list(res.keys())[0]
        valor = res[clave]
        messagebox.showinfo(clave, valor)
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
        id = self.id_producto.get()
        nombre = self.nombre.get()
        precio = self.precio.get()
        iva = self.iva.get()
        nota = self.nota.get()
        res = editar_producto(id, nombre, precio, iva, nota)
        clave = list(res.keys())[0]
        valor = res[clave]
        messagebox.showinfo(clave, valor)
        self.setTable()

    def eliminar(self):
        id = self.id_producto.get()
        res = eliminar_producto(id)
        clave = list(res.keys())[0]
        valor = res[clave]
        messagebox.showinfo(clave, valor)
        self.setTable()

    def limpiar(self):
        self.id_producto.set("")
        self.nombre.set("")
        self.precio.set("")
        self.iva.set("")
        self.nota.set("")

    def setTable(self):
        productos = getProductos()
        for p in self.tabla.get_children():
            self.tabla.delete(p)
        for p in productos:
            row = (p['id'], p['nombre'], p['precio'], p['iva'], p['nota'])
            self.tabla.insert("", "end", values=row)