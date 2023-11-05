from tkinter import messagebox

def v_enguardar(id, oldpass, newpass, confirm):
    if not id or not oldpass or not newpass or not confirm:
        messagebox.showinfo("Error", "Campos vacios")
        return False
    messagebox.showinfo("Success", "Cambio de clave exitoso")
    return True