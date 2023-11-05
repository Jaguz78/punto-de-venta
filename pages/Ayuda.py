import tkinter as tk

class AyudaForm(tk.Frame):
    def __init__(self, master, userSession):
        super().__init__(master)
        self.master = master
        self.userSession = userSession
        self.master.title("Sistema de Facturación")

        tk.Label(self, text="SISTEMA DE FACTURACIÓN GG", font=(24)).grid(row=0, pady=15, padx=295)
        tk.Label(self, text="Edgar Anthony Enmanuel Gonzalez López - 202146223").grid(row=1)
        tk.Label(self, text="José Alejandro Guzmán Heinemann - 202140561").grid(row=2)
        tk.Label(self, text="Archivos - Sexto Semestre 2023").grid(row=3)
        self.grid_columnconfigure(0, weight=1)