from tkinter import messagebox

def v_enagregarp(producto, cantidad):
    if not producto or not cantidad:
        messagebox.showinfo("Error", "Campos vacios")
        return False
    return True

def v_enguardar(fecha, cliente):
    if not fecha or not cliente:
        messagebox.showinfo("Error", "Campos vacios")
        return False
    messagebox.showinfo("Success", "La Factura fue creada exitosamente")
    return True 