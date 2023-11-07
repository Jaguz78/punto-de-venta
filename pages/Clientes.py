import tkinter as tk
from tkinter import ttk
from controllers.clientes import *
from tkcalendar import DateEntry
from tkinter import messagebox
from utils import *
from validaciones.v_clientes import *

class ClientesForm(tk.Frame):
    def __init__(self, master, userSession):
        super().__init__(master)
        self.master = master
        self.userSession = userSession
        self.master.title("Gestión de Clientes")

        self.id_cliente = tk.StringVar() ###
        self.identificacion = tk.StringVar()
        self.nombres = tk.StringVar()
        self.apellidos = tk.StringVar()
        self.direccion = tk.StringVar()
        self.telefono = tk.StringVar()
        self.ciudad = tk.StringVar()
        self.nacimiento = tk.StringVar()
        self.ingreso = tk.StringVar()
        self.nit = tk.StringVar()
        self.id = tk.StringVar()

        self.identificaciones = self.fillIdentificacion()
        self.ciudades = self.fillCiudad()

        self.crear_vista()
    
    def fillIdentificacion(self):
        identificacion = getIdentificaciones()
        ident = []
        for i in identificacion:
            ident.append(i[1])
        return ident
    
    def fillCiudad(self):
        ciudad = getCiudades()
        ciudades = []
        for c in ciudad:
            ciudades.append(c[1])
        return ciudades

    def crear_vista(self):
        tk.Label(self, text="Id a buscar:").grid(row=0, column=0, sticky="e", pady=20) 
        tk.Entry(self, textvariable=self.id, width=30).grid(row=0, column=1, padx=(10,20), pady=20)
        tk.Button(self, text="Buscar", command=self.encontrar).grid(row=0, column=2, pady=20)

        tk.Label(self, text="Nit:").grid(row=1, column=0, sticky="e", pady=8)
        tk.Entry(self, textvariable=self.nit, width=30).grid(row=1, column=1, padx=(10,20), pady=8)

        tk.Label(self, text="Nombres:").grid(row=2, column=0, sticky="e", pady=8)
        tk.Entry(self, textvariable=self.nombres, width=30).grid(row=2, column=1, padx=(10,20), pady=8)

        tk.Label(self, text="Apellidos:").grid(row=2, column=2, sticky="e", pady=8)
        tk.Entry(self, textvariable=self.apellidos, width=30).grid(row=2, column=3, padx=(10,20), pady=8)
        
        tk.Label(self, text="Dirección:").grid(row=3, column=0, sticky="e", pady=8)
        tk.Entry(self, textvariable=self.direccion, width=30).grid(row=3, column=1, padx=(10,20), pady=8)

        tk.Label(self, text="Identificación:").grid(row=3, column=2, sticky="e", pady=8)
        tk.OptionMenu(self, self.identificacion, *self.identificaciones).grid(row=3, column=3, padx=(10,20), pady=8)

        tk.Label(self, text="Teléfono:").grid(row=4, column=0, sticky="e", pady=8)
        tk.Entry(self, textvariable=self.telefono, width=30).grid(row=4, column=1, padx=(10,20), pady=8)

        tk.Label(self, text="Ciudad:").grid(row=4, column=2, sticky="e", pady=8)
        tk.OptionMenu(self, self.ciudad, *self.ciudades).grid(row=4, column=3, padx=(10,20), pady=8)

        tk.Label(self, text="Nacimiento:").grid(row=5, column=0, sticky="e", pady=8)
        DateEntry(self, textvariable=self.nacimiento, date_pattern="dd/mm/y").grid(row=5, column=1, padx=(10,20), pady=8)

        tk.Label(self, text="Ingreso:").grid(row=5, column=2, sticky="e", pady=8)
        DateEntry(self, textvariable=self.ingreso, date_pattern="dd/mm/y").grid(row=5, column=3, padx=(10,20), pady=8)

        tk.Button(self, text="Agregar", command=self.agregar).grid(row=6, column=0, pady=8)
        tk.Button(self, text="Editar", command=self.editar).grid(row=6, column=1, pady=8)
        tk.Button(self, text="Eliminar", command=self.eliminar).grid(row=6, column=2, pady=8)
        tk.Button(self, text="Limpiar", command=self.limpiar).grid(row=6, column=3, pady=8)

        self.tabla = ttk.Treeview(self, columns=("Id Cliente", "Identificación", "Nombres", "Apellidos", "Nit", "Dirección", "Teléfono", "Ciudad", "Nacimiento", "Ingreso"), show="headings")
        self.tabla.heading("#1", text="Id Cliente")
        self.tabla.heading("#2", text="Identificación")
        self.tabla.heading("#3", text="Nombres")
        self.tabla.heading("#4", text="Apellidos")
        self.tabla.heading("#5", text="Nit")
        self.tabla.heading("#6", text="Dirección")
        self.tabla.heading("#7", text="Teléfono")
        self.tabla.heading("#8", text="Ciudad")
        self.tabla.heading("#9", text="Nacimiento")
        self.tabla.heading("#10", text="Ingreso")
        self.tabla.column("#1", width=80, anchor="center")
        self.tabla.column("#2", width=120, anchor="center")
        self.tabla.column("#3", width=120, anchor="center")
        self.tabla.column("#4", width=120, anchor="center")
        self.tabla.column("#5", width=80, anchor="center")
        self.tabla.column("#6", width=150, anchor="center")
        self.tabla.column("#7", width=80, anchor="center")
        self.tabla.column("#8", width=80, anchor="center")
        self.tabla.column("#9", width=80, anchor="center")
        self.tabla.column("#10", width=80, anchor="center")
        self.tabla.grid(row=7, columnspan=9, pady=8)

        self.setTable()

        self.tabla.bind("<ButtonRelease-1>", self.buscar)

        tk.Button(self, text="<-", command=lambda: retroceder(self.tabla), width=5, pady=10).grid(row=8, column=1, pady=15)
        tk.Button(self, text="<<-", command=lambda: retrocederTodo(self.tabla), width=5, pady=10).grid(row=8, column=2, pady=15)
        tk.Button(self, text="->>", command=lambda: avanzarTodo(self.tabla), width=5, pady=10).grid(row=8, column=3, pady=15)
        tk.Button(self, text="->", command=lambda: avanzar(self.tabla), width=5, pady=10).grid(row=8, column=4, pady=15)
    
    def agregar(self):
        id = self.id_cliente.get() ###
        nit = self.nit.get()
        identificacion = self.identificacion.get()
        nombres = self.nombres.get()
        apellidos = self.apellidos.get()
        direccion = self.direccion.get()
        telefono = self.telefono.get()
        ciudad = self.ciudad.get()
        nacimiento = self.nacimiento.get()
        ingreso = self.ingreso.get()
        if v_enguardar(identificacion, nombres, apellidos, nit, direccion, telefono, ciudad, nacimiento, ingreso):
            agregar_cliente(nombres, apellidos, direccion, telefono, ciudad, identificacion, nacimiento, ingreso, nit)
            self.setTable()

    def buscar(self, event):
        item = self.tabla.selection()[0]
        values = self.tabla.item(item, "values")
        if values:
            #self.id_cliente.set(values[0]) ###
            self.identificacion.set(values[1])
            self.nombres.set(values[2])
            self.apellidos.set(values[3])
            self.nit.set(values[4])
            self.direccion.set(values[5])
            self.telefono.set(values[6])
            self.ciudad.set(values[7])
            self.nacimiento.set(values[8])
            self.ingreso.set(values[9])

    def editar(self):
        id = self.id_cliente.get() ###
        identificacion = self.identificacion.get()
        nombres = self.nombres.get()
        apellidos = self.apellidos.get()
        direccion = self.direccion.get()
        nit = self.nit.get()
        telefono = self.telefono.get()
        ciudad = self.ciudad.get()
        nacimiento = self.nacimiento.get()
        ingreso = self.ingreso.get()
        if v_eneditar(identificacion, nombres, apellidos, nit, direccion, telefono, ciudad, nacimiento, ingreso):
            editar_cliente(nombres, apellidos, direccion, telefono, ciudad, identificacion, nacimiento, ingreso, nit, id)
            self.setTable()

    def eliminar(self):
        id = self.id_cliente.get() ###
        if v_eneliminar(id):
            eliminar_cliente(id)
            self.setTable()

    def limpiar(self):
        self.id_cliente.set("") ###
        self.identificacion.set("")
        self.nombres.set("")
        self.apellidos.set("")
        self.nit.set("")
        self.direccion.set("")
        self.telefono.set("")
        self.ciudad.set("")
        self.nacimiento.set("")
        self.ingreso.set("")
        self.id.set("")

    def setTable(self):
        clientes = getClientes()
        for c in self.tabla.get_children():
            self.tabla.delete(c)
        for c in clientes:
            row = (c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8], c[9])
            self.tabla.insert("", "end", values=row)

    def encontrar(self):
        clientes = getClientes()
        id = self.id.get()
        if not id:
            messagebox.showinfo("Error", "Campo Vacio")
            return False
        for c in clientes:
            if c[0] == int(id):
                self.identificacion.set(c[1])
                self.nombres.set(c[2])
                self.apellidos.set(c[3])
                self.nit.set(c[4])
                self.direccion.set(c[5])
                self.telefono.set(c[6])
                self.ciudad.set(c[7])
                self.nacimiento.set(c[8])
                self.ingreso.set(c[9])
                messagebox.showinfo("Success", "El Cliente fue encontrado exitosamente")
                return True
        messagebox.showinfo("Error", "El Cliente no fue encontrado")
        return False