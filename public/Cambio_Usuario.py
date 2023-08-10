import tkinter as tk

class CambioUsuarioForm(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.label = tk.Label(self, text="CAMBIO DE USUARIO", font=("Helvetica", 20))
        self.label.pack(padx=20, pady=20)