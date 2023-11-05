from controllers.productos import *
from tkinter import messagebox

def v_enguardar(nombre, precio, iva, nota):
    if not nombre or not precio or not iva or not nota:
        messagebox.showinfo("Error", "Campos vacios")
        return False
    messagebox.showinfo("Success", "El Producto fue agregado exitosamente")
    return True

def v_eneditar(id, nombre, precio, iva, nota):
    if not id or not nombre or not precio or not iva or not nota:
        messagebox.showinfo("Error", "Campos vacios")
        return False
    messagebox.showinfo("Success", "El Producto fue editado exitosamente")
    return True

def v_eneliminar(id):
    productos = getProductos()
    if not id:
        messagebox.showinfo("Error", "Ingrese Id")
        return False
    for p in productos:
        if p['id'] == id:
            messagebox.showinfo("Success", "El Producto fue eliminado exitosamente")
            return True
    messagebox.showinfo("Error", "El Producto no fue encontrado")
    return False