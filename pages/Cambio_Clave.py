import tkinter as tk
from tkinter import messagebox
from validaciones.v_cambioclave import *

class CambioClaveForm(tk.Frame):
    def __init__(self, master, userSession):
        super().__init__(master)
        self.master = master
        self.userSession = userSession
        self.master.title("Cambio de clave")

        self.id_usuario = tk.StringVar()
        self.clave_actual = tk.StringVar()
        self.nueva_clave = tk.StringVar()
        self.confirmacion_clave = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Id Usuario:").grid(row=0, column=0, pady=10)
        tk.Entry(self, textvariable=self.id_usuario).grid(row=0, column=1, pady=10)

        tk.Label(self, text="Clave Actual:").grid(row=1, column=0, pady=10)
        tk.Entry(self, textvariable=self.clave_actual, show="*").grid(row=1, column=1, pady=10)

        tk.Label(self, text="Clave Nueva:").grid(row=2, column=0, pady=10)
        tk.Entry(self, textvariable=self.nueva_clave, show="*").grid(row=2, column=1, pady=10)

        tk.Label(self, text="Confirmar Clave:").grid(row=3, column=0, pady=10)
        tk.Entry(self, textvariable=self.confirmacion_clave, show="*").grid(row=3, column=1, pady=10)

        tk.Button(self, text="Guardar", command=self.save_user).grid(row=5, column=0, pady=10)
        tk.Button(self, text="Cancelar", command=self.clear_fields).grid(row=5, column=1, pady=10)

    def clear_fields(self):
        self.id_usuario.set("")
        self.clave_actual.set("")
        self.nueva_clave.set("")
        self.confirmacion_clave.set("")

    def save_user(self):
        id = self.id_usuario.get()
        oldpass = self.clave_actual.get()
        newpass = self.nueva_clave.get()
        confirm = self.confirmacion_clave.get()
        if v_enguardar(id, oldpass, newpass, confirm):
            ###
            res = self.userSession.changePassword(id, oldpass, newpass, confirm)
            clave = list(res.keys())[0]
            valor = res[clave]
            messagebox.showinfo(clave, valor)