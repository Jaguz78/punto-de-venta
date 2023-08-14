import tkinter as tk

class NuevaFacturaForm(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.label = tk.Label(self, text="NUEVA FACTURA", font=("Helvetica", 20))
        self.label.pack(padx=20, pady=20)