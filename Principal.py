# Views
from tkinter import *
from pages.Ayuda import *
from pages.Cambio_Clave import *
from pages.Clientes import *
from pages.Nueva_Factura import *
from pages.Productos import *
from pages.Reporte_Facturas import *
from pages.Usuarios import *    
from controllers.session import UserSession

class LoginWindow:
    def __init__(self, ventana, userSession):
        self.ventana = ventana
        self.userSession = userSession
        self.ventana.title("Login")
        self.ventana.geometry("400x300")

        self.frame1 = tk.Frame(ventana, bg="#3498db")
        self.frame1.pack(side=tk.TOP, fill=tk.X)

        self.frame2 = tk.Frame(ventana)
        self.frame2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.mostrar_contenido()

    def mostrar_contenido(self):
        self.frame2.destroy()
        self.frame2 = LoginPanel(self.ventana, self.userSession)
        self.frame2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


class LoginPanel(tk.Frame):
    def __init__(self, parent, userSession):
        super().__init__(parent)
        self.userSession = userSession
        self.parent = parent

        self.configure(bg="#f2f2f2")  # Fondo más claro
        
        self.label_username = tk.Label(self, text="ID Usuario:", bg="#f2f2f2")
        self.label_password = tk.Label(self, text="Contraseña:", bg="#f2f2f2")
        
        self.entry_username = ttk.Entry(self)
        self.entry_password = ttk.Entry(self, show="*")
        
        self.button_login = ttk.Button(self, text="Iniciar Sesión", command=self.login2)
        
        self.label_username.pack(pady=10)
        self.entry_username.pack(pady=5)
        self.label_password.pack(pady=10)
        self.entry_password.pack(pady=5)
        self.button_login.pack(pady=20)
        
        self.pack(fill=tk.BOTH, expand=True)

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

class App:
    def __init__(self, ventana, userSession):
        self.ventana = ventana
        self.userSession = userSession
        self.ventana.title("SISTEMA DE FACTURACIÓN")
        self.ventana.geometry("1000x650")

        self.frame1 = tk.Frame(ventana, bg="#3498db")
        self.frame1.pack(side=tk.TOP, fill=tk.X)

        menu_principal = tk.Menu(self.frame1)

        menu_archivo = tk.Menu(menu_principal, tearoff=0)
        menu_archivo.add_command(label="Clientes", command=lambda: self.mostrar_contenido(ClientesForm))
        menu_archivo.add_command(label="Productos", command=lambda: self.mostrar_contenido(ProductosForm))
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Cambio Clave", command=lambda: self.mostrar_contenido(CambioClaveForm))
        menu_archivo.add_command(label="Cambio Usuario", command=self.cambio_usuario)
        if self.userSession.get_role() == 'admin':
            menu_archivo.add_command(label="Usuarios", command=lambda: self.mostrar_contenido(UsuariosForm))
            menu_archivo.add_separator()
            menu_archivo.add_command(label="Salir", command=ventana.quit)

        menu_movimientos = tk.Menu(menu_principal, tearoff=0)
        menu_movimientos.add_command(label="Nueva Factura", command=lambda: self.mostrar_contenido(NuevaFacturaForm))
        if self.userSession.get_role() == 'admin':
            menu_movimientos.add_command(label="Reporte Facturas", command=lambda: self.mostrar_contenido(ReporteFacturasForm))

        menu_ayuda = tk.Menu(menu_principal, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=lambda: self.mostrar_contenido(AyudaForm))

        menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
        menu_principal.add_cascade(label="Movimientos", menu=menu_movimientos)
        menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)

        self.ventana.config(menu=menu_principal)
        
        self.frame2 = tk.Frame(ventana)
        self.frame2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def mostrar_contenido(self, frame_class):
        self.frame2.destroy()
        self.frame2 = frame_class(self.ventana, self.userSession)
        self.frame2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def cambio_usuario(self):
        self.userSession.logout()
        self.ventana.destroy()
        newVentana = tk.Tk()
        LoginWindow(newVentana, self.userSession)
        newVentana.mainloop()

if __name__ == "__main__":
    userSession = UserSession()
    ventana = tk.Tk()
    login = LoginWindow(ventana, userSession)
    app = App(ventana, userSession)
    ventana.mainloop()