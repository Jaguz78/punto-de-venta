from controllers.clientes import *
from tkinter import messagebox

def v_enguardar(identificacion, nombres, apellidos, nit, direccion, telefono, ciudad, nacimiento, ingreso):
    clientes = getClientes()
    if not identificacion or not nombres or not apellidos or not nit or not direccion or not telefono or not ciudad or not nacimiento or not ingreso:
        messagebox.showinfo("Error", "Campos vacios")
        return False
    for c in clientes:
        if c['nit'] == nit:
            messagebox.showinfo("Error", "Nit ya registrado")
            return False
    messagebox.showinfo("Success", "El Cliente fue agregado exitosamente")
    return True

def v_eneditar(identificacion, nombres, apellidos, nit, direccion, telefono, ciudad, nacimiento, ingreso):
    if not identificacion or not nombres or not apellidos or not nit or not direccion or not telefono or not ciudad or not nacimiento or not ingreso:
        messagebox.showinfo("Error", "Campos vacios")
        return False
    messagebox.showinfo("Success", "El Cliente fue editado exitosamente")
    return True

def v_eneliminar(id):
    clientes = getClientes()
    if not id:
        messagebox.showinfo("Error", "Ingrese Id")
        return False
    for c in clientes:
        if c['id'] == id:
            messagebox.showinfo("Success", "El Cliente fue eliminado exitosamente")
            return True
    messagebox.showinfo("Error", "El Cliente no fue encontrado")
    return False