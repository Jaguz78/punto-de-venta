from dbConnection import establecer_conexion

conexion = establecer_conexion()

def getUsers():
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos')
    return cursor

def createUser(id, name, lastname, perfil, password, direccion, telefono):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios (id, nombres, apellidos, id_perfil, clave, direccion, telefono) VALUES (?,?,?,?,?,?,?)",\
        id, name, lastname, perfil, password, direccion, telefono)
    conexion.commit()
    cursor.close()
    
def deleteUser(id):
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id=?", id)
    conexion.commit()
    cursor.close()

def editUser(id, name, lastname, perfil, password, direccion, telefono):
    cursor = conexion.cursor()
    cursor.execute("UPDATE usuarios SET nombres=?, apellidos=?, id_perfil=?, clave=?, direccion=?, telefono=? WHERE id=?",\
        name, lastname, perfil, password, direccion, telefono, id)
    conexion.commit()
    cursor.close()   