from dbConnection import establecer_conexion

conexion = establecer_conexion()

def getProductos():
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos')
    return cursor

def agregar_producto(nombre, precio, iva, nota):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (nombre, id_iva, nota, precio) VALUES (?,?,?,?)",\
        nombre, precio, iva, nota)
    conexion.commit()
    cursor.close()

def editar_producto(id, nombre, precio, iva, nota):
    cursor = conexion.cursor()
    cursor.execute("UPDATE productos SET nombre=?, id_iva=?, nota=?, precio=? WHERE id=?",\
        nombre, iva, nota, precio, id)
    conexion.commit()
    cursor.close()

def eliminar_producto(id):
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id=?", id)
    conexion.commit()
    cursor.close()