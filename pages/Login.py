import tkinter as tk

class LoginPanel(tk.Frame):
    def __init__(self, parent, userSession):
        super().__init__(parent)
        self.userSession = userSession
        
        self.label_username = tk.Label(self, text="Usuario:")
        self.label_password = tk.Label(self, text="Contraseña:")
        
        self.entry_username = tk.Entry(self)
        self.entry_password = tk.Entry(self, show="*")
        
        self.button_login = tk.Button(self, text="Iniciar Sesión", command=lambda: print(userSession.login(self.entry_username.get(), self.entry_password.get())))
        
        self.label_username.pack(pady=10)
        self.entry_username.pack(pady=5)
        self.label_password.pack(pady=10)
        self.entry_password.pack(pady=5)
        self.button_login.pack(pady=20)
        
        self.pack()