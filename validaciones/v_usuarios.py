from controllers.users import *
from tkinter import messagebox

def v_enguardar(id, name, lastname, perfil, password, confirm, direccion, telefono):
    usuarios = getUsers()
    if not id or not name or not lastname or not perfil or not password or not confirm or not direccion or not telefono:
        messagebox.showinfo("Error", "Campos vacios")
        return False
    for u in usuarios:
        if u['id'] == id:
            messagebox.showinfo("Error", "Id ya registrado")
            return False
    if password != confirm:
        messagebox.showinfo("Error", "Las claves no coinciden")
        return False
    messagebox.showinfo("Success", "El Usuario fue registrado exitosamente")
    return True

def v_eneditar(id, name, lastname, perfil, password, direccion, telefono):
    if not id or not name or not lastname or not perfil or not password or not direccion or not telefono:
        messagebox.showinfo("Error", "Campos vacios")
        return False
    messagebox.showinfo("Success", "El Usuario fue editado exitosamente")
    return True

def v_eneliminar(id):
    usuarios = getUsers()
    if not id:
        messagebox.showinfo("Error", "Ingrese Id")
        return False
    for u in usuarios:
        if u['id'] == id:
            messagebox.showinfo("Success", "El Usuario fue eliminado exitosamente")
            return True
    messagebox.showinfo("Error", "El Usuario no fue encontrado")
    return False