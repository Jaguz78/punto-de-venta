import tkinter as tk

class AyudaForm(tk.Frame):
    def __init__(self, root, userSession):
        super().__init__(root)
        self.userSession = userSession
        
        self.label = tk.Label(self, text="ACERCA DE", font=("Helvetica", 20))
        self.label.pack(padx=20, pady=20)