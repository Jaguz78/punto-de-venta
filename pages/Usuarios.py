import tkinter as tk
from tkinter import ttk
from controllers.users import *
from tkinter import messagebox
from utils import *
from validaciones.v_usuarios import *

class UsuariosForm(tk.Frame):
    def __init__(self, master, userSession):
        super().__init__(master)
        self.master = master
        self.userSession = userSession
        self.master.title("Gestión de Usuarios")

        self.id = tk.StringVar()
        self.id_usuario = tk.StringVar()
        self.nombres = tk.StringVar()
        self.apellidos = tk.StringVar()
        self.clave = tk.StringVar()
        self.confirmacion_clave = tk.StringVar()
        self.perfil = tk.StringVar()
        self.direccion = tk.StringVar()
        self.telefono = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Id a buscar:").grid(row=0, column=0, pady=20) 
        tk.Entry(self, textvariable=self.id, width=30).grid(row=0, column=1, padx=(10,20), pady=20)
        tk.Button(self, text="Buscar", command=self.encontrar).grid(row=0, column=2, pady=20)

        tk.Label(self, text="Id Usuario:").grid(row=1, column=0, pady=8) 
        tk.Entry(self, textvariable=self.id_usuario, width=30).grid(row=1, column=1, padx=(10,20), pady=8)

        tk.Label(self, text="Perfil:").grid(row=1, column=2, pady=8)
        tk.OptionMenu(self, self.perfil, "vendedor", "admin").grid(row=1, column=3, pady=8)

        tk.Label(self, text="Nombres:").grid(row=2, column=0, pady=8)
        tk.Entry(self, textvariable=self.nombres, width=30).grid(row=2, column=1, padx=(10,20), pady=8)

        tk.Label(self, text="Apellidos:").grid(row=2, column=2, pady=8)
        tk.Entry(self, textvariable=self.apellidos, width=30).grid(row=2, column=3, padx=(10, 20), pady=8)

        tk.Label(self, text="Clave:").grid(row=3, column=0, pady=8)
        tk.Entry(self, textvariable=self.clave, show="*", width=30).grid(row=3, column=1, padx=(10, 20), pady=8)

        tk.Label(self, text="Confirmar Clave:").grid(row=3, column=2, pady=8)
        tk.Entry(self, textvariable=self.confirmacion_clave, show="*", width=30).grid(row=3, column=3, padx=(10, 20), pady=8)

        tk.Label(self, text="Dirección:").grid(row=4, column=0, pady=8)
        tk.Entry(self, textvariable=self.direccion, width=30).grid(row=4, column=1, padx=(10,20), pady=8)

        tk.Label(self, text="Telefono:").grid(row=4, column=2, pady=8)
        tk.Entry(self, textvariable=self.telefono, width=30).grid(row=4, column=3, padx=(10, 20), pady=8)

        tk.Button(self, text="Guardar", command=self.save_user).grid(row=5, column=1, pady=8)
        tk.Button(self, text="Borrar", command=self.delete_user).grid(row=5, column=2, pady=8)
        tk.Button(self, text="Editar", command=self.edit_user).grid(row=5, column=3, pady=8)
        tk.Button(self, text="Cancelar", command=self.clear_fields).grid(row=5, column=4, pady=8)

        self.user_table = ttk.Treeview(self, columns=("ID", "Nombres", "Apellidos", "Perfil", "Dirección", "Telefono"), show="headings")
        self.user_table.heading("#1", text="ID")
        self.user_table.heading("#2", text="Nombres")
        self.user_table.heading("#3", text="Apellidos")
        self.user_table.heading("#4", text="Perfil")
        self.user_table.heading("#5", text="Dirección")
        self.user_table.heading("#6", text="Telefono")
        self.user_table.column("#1", width=100, anchor="center")
        self.user_table.column("#2", width=200, anchor="center")
        self.user_table.column("#3", width=200, anchor="center")
        self.user_table.column("#4", width=150, anchor="center")
        self.user_table.column("#5", width=200, anchor="center")
        self.user_table.column("#6", width=150, anchor="center")
        self.user_table.grid(row=6, columnspan=6, pady=8)

        self.setTable()

        tk.Button(self, text="<-", command=lambda: retroceder(self.user_table), width=5, pady=10).grid(row=7, column=1, pady=15)
        tk.Button(self, text="<<-", command=lambda: retrocederTodo(self.user_table), width=5, pady=10).grid(row=7, column=2, pady=15)
        tk.Button(self, text="->>", command=lambda: avanzarTodo(self.user_table), width=5, pady=10).grid(row=7, column=3, pady=15)
        tk.Button(self, text="->", command=lambda: avanzar(self.user_table), width=5, pady=10).grid(row=7, column=4, pady=15)
        
        self.user_table.bind("<ButtonRelease-1>", self.search_user)

    def clear_fields(self):
        self.id_usuario.set("")
        self.nombres.set("")
        self.apellidos.set("")
        self.clave.set("")
        self.confirmacion_clave.set("")
        self.perfil.set("")
        self.direccion.set("")
        self.telefono.set("")
        self.id.set("")

    def edit_user(self):
        id = self.id_usuario.get()
        name = self.nombres.get()
        lastname = self.apellidos.get()
        password = self.clave.get()
        perfil = self.perfil.get()
        direccion = self.direccion.get()
        telefono = self.telefono.get()
        idPerfil = buscar_idPerfil(perfil)
        if v_eneditar(id, name, lastname, perfil, password, direccion, telefono):
            editUser(id, name, lastname, idPerfil[0][0], password, direccion, telefono)
            self.setTable()

    def save_user(self):
        id = self.id_usuario.get()
        name = self.nombres.get()
        lastname = self.apellidos.get()
        password = self.clave.get()
        confirm = self.confirmacion_clave.get()
        perfil = self.perfil.get()
        direccion = self.direccion.get()
        telefono = self.telefono.get()
        idPerfil = buscar_idPerfil(perfil)
        if v_enguardar(id, name, lastname, perfil, password, confirm, direccion, telefono):
            createUser(id, name, lastname, idPerfil[0][0], password, direccion, telefono)
            self.setTable()
            
    def delete_user(self):
        id = self.id_usuario.get()
        if v_eneliminar(id):
            deleteUser(id)
            self.setTable()

    def setTable(self):
        users = getUsers()
        self.user_table.delete(*self.user_table.get_children())
        for u in users:
            row = (u[0], u[1], u[2], u[3], u[4], u[5])
            self.user_table.insert("", "end", values=row)

    def search_user(self, event):
        item = self.user_table.selection()[0]
        values = self.user_table.item(item, "values")
        if values:
            self.id_usuario.set(values[0])
            self.nombres.set(values[1])
            self.apellidos.set(values[2])
            self.perfil.set(values[3])
            self.direccion.set(values[4])
            self.telefono.set(values[5])
    
    def encontrar(self):
        users = getUsers()
        id = self.id.get()
        if not id:
            messagebox.showinfo("Error", "Campo Vacio")
            return False
        for u in users:
            if u[0] == id:
                self.id_usuario.set(u[0])
                self.nombres.set(u[1])
                self.apellidos.set(u[2])
                self.perfil.set(u[3])
                self.direccion.set(u[4])
                self.telefono.set(u[5])
                messagebox.showinfo("Success", "El Usuario fue encontrado exitosamente")
                return True
        messagebox.showinfo("Error", "El Usuario no fue encontrado")
        return False