import tkinter as tk
from Principal import App
from .Ayuda import AyudaForm
from tkinter import messagebox

class LoginWindow:
    def __init__(self, ventana, userSession):
        self.ventana = ventana
        self.userSession = userSession
        self.ventana.title("Login")
        self.ventana.geometry("900x600")

        self.frame1 = tk.Frame(ventana)
        self.frame1.pack(side=tk.TOP, fill=tk.X)

        self.frame2 = tk.Frame(ventana)
        self.frame2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def mostrar_contenido(self, frame_class):
        self.frame2.destroy()
        self.frame2 = frame_class(self.ventana, self.userSession)
        self.frame2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


class LoginPanel(tk.Frame):
    def __init__(self, parent, userSession):
        super().__init__(parent)
        self.userSession = userSession
        self.parent =  parent
        
        self.label_username = tk.Label(self, text="ID Usuario:")
        self.label_password = tk.Label(self, text="Contraseña:")
        
        self.entry_username = tk.Entry(self)
        self.entry_password = tk.Entry(self, show="*")
        
        self.button_login = tk.Button(self, text="Iniciar Sesión", command=lambda: self.login2())
        
        self.label_username.pack(pady=10)
        self.entry_username.pack(pady=5)
        self.label_password.pack(pady=10)
        self.entry_password.pack(pady=5)
        self.button_login.pack(pady=20)
        
        self.pack()

    def login2(self):
        res = self.userSession.login(self.entry_username.get(), self.entry_password.get())
        if self.userSession.is_logged_in():
            self.openMainWindow()
        else:
            messagebox.showerror("Error", res["error"])

    def openMainWindow(self):
        if self.userSession.is_logged_in():
            self.parent.destroy()
            ventana = tk.Tk()
            app = App(ventana, self.userSession)
            app.mostrar_contenido(AyudaForm)