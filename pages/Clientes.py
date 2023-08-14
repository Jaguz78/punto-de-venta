import tkinter as tk

class ClientesForm(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.label = tk.Label(self, text="CLIENTES", font=("Helvetica", 20))
        self.label.pack(padx=20, pady=20)