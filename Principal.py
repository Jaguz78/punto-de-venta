# Views
from tkinter import *
from pages.Ayuda import *
from pages.Cambio_Clave import *
from pages.Cambio_Usuario import *
from pages.Clientes import *
from pages.Nueva_Factura import *
from pages.Productos import *
from pages.Reporte_Facturas import *
from pages.Usuarios import *
from pages.Login import *
from controllers.session import UserSession

class App:
    def __init__(self, ventana, userSession):
        self.ventana = ventana
        self.userSession = userSession
        self.ventana.title("SISTEMA DE FACTURACIÓN")
        self.ventana.geometry("900x600")

        self.frame1 = tk.Frame(ventana)
        self.frame1.pack(side=tk.TOP, fill=tk.X)

        menu_principal = Menu(self.frame1)

        menu_archivo = Menu(menu_principal, tearoff=0)
        menu_archivo.add_command(label="Clientes", command=lambda: self.mostrar_contenido(ClientesForm))
        menu_archivo.add_command(label="Productos", command=lambda: self.mostrar_contenido(ProductosForm))
        menu_archivo.add_separator()
        if self.userSession.get_role() == 'admin':
            menu_archivo.add_command(label="Usuarios", command=lambda: self.mostrar_contenido(UsuariosForm))
            menu_archivo.add_command(label="Cambio Clave", command=lambda: self.mostrar_contenido(CambioClaveForm))
            menu_archivo.add_command(label="Cambio Usuario", command=lambda: self.mostrar_contenido(CambioUsuarioForm))
            menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=ventana.quit)

        menu_movimientos = Menu(menu_principal, tearoff=0)
        menu_movimientos.add_command(label="Nueva Factura", command=lambda: self.mostrar_contenido(NuevaFacturaForm))
        if self.userSession.get_role() == 'admin':
            menu_movimientos.add_command(label="Reporte Facturas", command=lambda: self.mostrar_contenido(ReporteFacturasForm))

        menu_ayuda = Menu(menu_principal, tearoff=0)
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

if __name__ == "__main__":
    userSession = UserSession()
    ventana = tk.Tk()
    login = LoginWindow(ventana, userSession)
    login.mostrar_contenido(LoginPanel)
    ventana.mainloop()