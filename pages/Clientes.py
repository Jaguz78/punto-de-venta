import tkinter as tk
from tkinter import ttk
from controllers.clientes import *
from tkcalendar import DateEntry
from tkinter import messagebox
from utils import *

class ClientesForm(tk.Frame):
    def __init__(self, master, userSession):
        super().__init__(master)
        self.master = master
        self.userSession = userSession
        self.master.title("Gestión de Clientes")

        self.id_cliente = tk.StringVar()
        self.identificacion = tk.StringVar()
        self.nombres = tk.StringVar()
        self.apellidos = tk.StringVar()
        self.direccion = tk.StringVar()
        self.telefono = tk.StringVar()
        self.ciudad = tk.StringVar()
        self.nacimiento = tk.StringVar()
        self.ingreso = tk.StringVar()

        self.crear_vista()
    
    def crear_vista(self):
        tk.Label(self, text="Id Cliente:").grid(row=0, column=0, sticky="e")
        tk.Entry(self, textvariable=self.id_cliente, width=30).grid(row=0, column=1, padx=(10,20))

        tk.Label(self, text="Identificación:").grid(row=0, column=2, sticky="e")
        tk.OptionMenu(self, self.identificacion, "DPI", "Pasaporte").grid(row=0, column=3, padx=(10,20))

        tk.Label(self, text=" ", height=1).grid(row=1)

        tk.Label(self, text="Nombres:").grid(row=2, column=0, sticky="e")
        tk.Entry(self, textvariable=self.nombres, width=30).grid(row=2, column=1, padx=(10,20))

        tk.Label(self, text=" ", height=1).grid(row=3)

        tk.Label(self, text="Apellidos:").grid(row=4, column=0, sticky="e")
        tk.Entry(self, textvariable=self.apellidos, width=30).grid(row=4, column=1, padx=(10,20))

        tk.Label(self, text=" ", height=1).grid(row=5)

        tk.Label(self, text="Dirección:").grid(row=6, column=0, sticky="e")
        tk.Entry(self, textvariable=self.direccion, width=30).grid(row=6, column=1, padx=(10,20))

        tk.Label(self, text=" ", height=1).grid(row=7)

        tk.Label(self, text="Teléfono:").grid(row=8, column=0, sticky="e")
        tk.Entry(self, textvariable=self.telefono, width=30).grid(row=8, column=1, padx=(10,20))

        tk.Label(self, text="Ciudad:").grid(row=8, column=2, sticky="e")
        tk.OptionMenu(self, self.ciudad, "Coban", "Carcha", "Chamelco", "Santa Cruz", "San Cristobal", "Tactic").grid(row=8, column=3, padx=(10,20))

        tk.Label(self, text=" ", height=1).grid(row=9)

        tk.Label(self, text="Nacimiento:").grid(row=10, column=0, sticky="e")
        DateEntry(self, textvariable=self.nacimiento, date_pattern="dd/mm/y").grid(row=10, column=1, padx=(10,20))

        tk.Label(self, text="Ingreso:").grid(row=10, column=2, sticky="e")
        DateEntry(self, textvariable=self.ingreso, date_pattern="dd/mm/y").grid(row=10, column=3, padx=(10,20))

        tk.Label(self, text=" ", height=1).grid(row=11)

        tk.Button(self, text="Agregar", command=self.agregar).grid(row=12, column=0)
        tk.Button(self, text="Editar", command=self.editar).grid(row=12, column=1)
        tk.Button(self, text="Eliminar", command=self.eliminar).grid(row=12, column=2)
        tk.Button(self, text="Limpiar", command=self.limpiar).grid(row=12, column=3)

        tk.Label(self, text=" ", height=1).grid(row=13)

        self.tabla = ttk.Treeview(self, columns=("Id Cliente", "Identificación", "Nombres", "Apellidos", "Dirección", "Teléfono", "Ciudad", "Nacimiento", "Ingreso"), show="headings")
        self.tabla.heading("#1", text="Id Cliente")
        self.tabla.heading("#2", text="Identificación")
        self.tabla.heading("#3", text="Nombres")
        self.tabla.heading("#4", text="Apellidos")
        self.tabla.heading("#5", text="Dirección")
        self.tabla.heading("#6", text="Teléfono")
        self.tabla.heading("#7", text="Ciudad")
        self.tabla.heading("#8", text="Nacimiento")
        self.tabla.heading("#9", text="Ingreso")
        self.tabla.column("#1", width=80, anchor="center")
        self.tabla.column("#2", width=120, anchor="center")
        self.tabla.column("#3", width=120, anchor="center")
        self.tabla.column("#4", width=120, anchor="center")
        self.tabla.column("#5", width=150, anchor="center")
        self.tabla.column("#6", width=80, anchor="center")
        self.tabla.column("#7", width=80, anchor="center")
        self.tabla.column("#8", width=80, anchor="center")
        self.tabla.column("#9", width=80, anchor="center")
        self.tabla.grid(row=14, columnspan=9)

        self.setTable()

        self.tabla.bind("<ButtonRelease-1>", self.buscar)

        # Flechitas
        tk.Button(self, text="<-", command=lambda: retroceder(self.tabla), width=5, pady=10).grid(row=15, column=1, pady=20)
        tk.Button(self, text="<<-", command=lambda: retrocederTodo(self.tabla), width=5, pady=10).grid(row=15, column=2, pady=20)
        tk.Button(self, text="->>", command=lambda: avanzarTodo(self.tabla), width=5, pady=10).grid(row=15, column=3, pady=20)
        tk.Button(self, text="->", command=lambda: avanzar(self.tabla), width=5, pady=10).grid(row=15, column=4, pady=20)
    
    def agregar(self):
        # id = self.id_cliente.get()
        identificacion = self.identificacion.get()
        nombres = self.nombres.get()
        apellidos = self.apellidos.get()
        direccion = self.direccion.get()
        telefono = self.telefono.get()
        ciudad = self.ciudad.get()
        nacimiento = self.nacimiento.get()
        ingreso = self.ingreso.get()
        res = agregar_cliente(nombres, apellidos, direccion, telefono, ciudad, identificacion, nacimiento, ingreso)
        # clave = list(res.keys())[0]
        # valor = res[clave]
        # messagebox.showinfo(clave, valor)
        self.setTable()

    def buscar(self, event):
        item = self.tabla.selection()[0]
        values = self.tabla.item(item, "values")
        if values:
            self.id_cliente.set(values[0])
            self.identificacion.set(values[1])
            self.nombres.set(values[2])
            self.apellidos.set(values[3])
            self.direccion.set(values[4])
            self.telefono.set(values[5])
            self.ciudad.set(values[6])
            self.nacimiento.set(values[7])
            self.ingreso.set(values[8])

    def editar(self):
        id = self.id_cliente.get()
        identificacion = self.identificacion.get()
        nombres = self.nombres.get()
        apellidos = self.apellidos.get()
        direccion = self.direccion.get()
        telefono = self.telefono.get()
        ciudad = self.ciudad.get()
        nacimiento = self.nacimiento.get()
        ingreso = self.ingreso.get()
        res = editar_cliente(id, identificacion, nombres, apellidos, direccion, telefono, ciudad, nacimiento, ingreso)
        clave = list(res.keys())[0]
        valor = res[clave]
        messagebox.showinfo(clave, valor)
        self.setTable()

    def eliminar(self):
        id = self.id_cliente.get()
        res = eliminar_cliente(id)
        clave = list(res.keys())[0]
        valor = res[clave]
        messagebox.showinfo(clave, valor)
        self.setTable()

    def limpiar(self):
        self.id_cliente.set("")
        self.identificacion.set("")
        self.nombres.set("")
        self.apellidos.set("")
        self.direccion.set("")
        self.telefono.set("")
        self.ciudad.set("")
        self.nacimiento.set("")
        self.ingreso.set("")

    def setTable(self):
        clientes = getClientes()
        for c in self.tabla.get_children():
            self.tabla.delete(c)
        for c in clientes:
            row = (c['id'], c['identificacion'], c['nombres'], c['apellidos'], c['direccion'], c['telefono'], c['ciudad'], c['nacimiento'], c['ingreso'])
            self.tabla.insert("", "end", values=row)