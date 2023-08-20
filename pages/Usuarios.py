import tkinter as tk
from tkinter import ttk
from controllers.users import *
from tkinter import messagebox

class UsuariosForm(tk.Frame):
    def __init__(self, master, userSession):
        super().__init__(master)
        self.master = master
        self.userSession = userSession
        self.master.title("Gestión de Usuarios")

        self.id_usuario = tk.StringVar()
        self.nombres = tk.StringVar()
        self.apellidos = tk.StringVar()
        self.clave = tk.StringVar()
        self.confirmacion_clave = tk.StringVar()
        self.perfil = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="ID Usuario:").grid(row=0, column=0)
        tk.Entry(self, textvariable=self.id_usuario).grid(row=0, column=1)

        tk.Label(self, text="Nombres:").grid(row=0, column=2)
        tk.Entry(self, textvariable=self.nombres).grid(row=0, column=3)

        tk.Label(self, text="Apellidos:").grid(row=1, column=2)
        tk.Entry(self, textvariable=self.apellidos).grid(row=1, column=3)

        tk.Label(self, text="Clave:").grid(row=1, column=0)
        tk.Entry(self, textvariable=self.clave, show="*").grid(row=1, column=1)

        tk.Label(self, text="Confirmar Clave:").grid(row=2, column=0)
        tk.Entry(self, textvariable=self.confirmacion_clave, show="*").grid(row=2, column=1)

        tk.Label(self, text="Perfil:").grid(row=2, column=2)
        tk.OptionMenu(self, self.perfil, "vendedor", "admin").grid(row=2, column=3)

        # Botones
        tk.Button(self, text="Editar", command=self.edit_user).grid(row=6, column=1)
        tk.Button(self, text="Guardar", command=self.save_user).grid(row=6, column=2)
        tk.Button(self, text="Borrar", command=self.delete_user).grid(row=6, column=3)
        tk.Button(self, text="Cancelar", command=self.clear_fields).grid(row=6, column=5)

        # Tabla
        self.user_table = ttk.Treeview(self, columns=("ID", "Nombres", "Apellidos", "Perfil"))
        self.user_table.heading("#1", text="ID")
        self.user_table.heading("#2", text="Nombres")
        self.user_table.heading("#3", text="Apellidos")
        self.user_table.heading("#4", text="Perfil")
        self.user_table.grid(row=7, columnspan=6)

        # Rellenar la tabla
        self.setTable()
        
        # Evento para buscar usuario en la tabla
        self.user_table.bind("<ButtonRelease-1>", self.search_user)


    def clear_fields(self):
        self.id_usuario.set("")
        self.nombres.set("")
        self.apellidos.set("")
        self.clave.set("")
        self.confirmacion_clave.set("")
        self.perfil.set("")

    def edit_user(self):
        id = self.id_usuario.get()
        name = self.nombres.get()
        lastname = self.apellidos.get()
        role = self.perfil.get()
        res = editUser(id, name, lastname, role)
        #Feedback
        clave = list(res.keys())[0]
        valor = res[clave]
        messagebox.showinfo(clave, valor)
        self.setTable()


    def save_user(self):
        id = self.id_usuario.get()
        name = self.nombres.get()
        lastname = self.apellidos.get()
        password = self.clave.get()
        confirm = self.confirmacion_clave.get()
        role = self.perfil.get()
        res = createUser(id, name, lastname, password, confirm, role)
        #Feedback
        clave = list(res.keys())[0]
        valor = res[clave]
        messagebox.showinfo(clave, valor)
        self.setTable()

    def delete_user(self):
        id = self.id_usuario.get()
        res = deleteUser(id)
        #Feedback
        clave = list(res.keys())[0]
        valor = res[clave]
        messagebox.showinfo(clave, valor)
        self.setTable()

    def setTable(self):
        users = getUsers()
        for u in users:
            row = (u['id'], u['name'], u['lastname'], u['role'])
            self.user_table.insert("", "end", values=row)

    def search_user(self, event):
        item = self.user_table.selection()[0]  # Obtener el elemento seleccionado
        values = self.user_table.item(item, "values")  # Obtener los valores de la fila
        if values:
            self.id_usuario.set(values[0])
            self.nombres.set(values[1])
            self.apellidos.set(values[2])
            self.perfil.set(values[3])
