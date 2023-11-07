from dbConnection import establecer_conexion

conexion = establecer_conexion()

def getProductos():
    cursor = conexion.cursor()
    cursor.execute('SELECT p.id, p.nombre, p.precio, i.porcentaje, p.nota FROM productos p INNER JOIN iva i ON p.id_iva = i.id')
    registros = cursor.fetchall()
    return registros

def getIva():
    cursor = conexion.cursor()
    cursor.execute('SELECT id, porcentaje FROM iva')
    registros = cursor.fetchall()
    return registros

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