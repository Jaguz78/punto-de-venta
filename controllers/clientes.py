from dbConnection import establecer_conexion

conexion = establecer_conexion()

def getClientes():
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM clientes')
    return cursor

def agregar_cliente(nombres, apellidos, direccion, telefono, ciudad, identificacion, nacimiento, ingreso):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO clientes (nombres, apellidos, dirección, telefono, id_ciudad, id_identificacion, fecha_nac, fecha_ingreso) VALUES (?,?,?,?,?,?,?,?)",\
        nombres, apellidos, direccion, telefono, ciudad, identificacion, nacimiento, ingreso)
    conexion.commit()
    cursor.close()

def editar_cliente(id, identificacion, nombres, apellidos, direccion, telefono, ciudad, nacimiento, ingreso):
    cursor = conexion.cursor()
    cursor.execute("UPDATE clientes SET nombres=?, apellidos=?, dirección=?, telefono=?, id_cuidad=?, id_identificacion=?, fecha_nac=?, fecha_ingreso=? WHERE id=?",\
        nombres, apellidos, direccion, telefono, ciudad, identificacion, nacimiento, ingreso, id)
    conexion.commit()
    cursor.close()

def eliminar_cliente(id):
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM clientes WHERE id=?", id)
    conexion.commit()
    cursor.close()