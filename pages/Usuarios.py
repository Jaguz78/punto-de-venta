import tkinter as tk

class UsuariosForm(tk.Frame):
    def __init__(self, root, userSession):
        super().__init__(root)
        self.userSession = userSession
        
        self.label = tk.Label(self, text="USUARIOS", font=("Helvetica", 20))
        self.label.pack(padx=20, pady=20)