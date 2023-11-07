from dbConnection import establecer_conexion

conexion = establecer_conexion()

def getClientes():
    cursor = conexion.cursor()
    cursor.execute('SELECT c.id, i.identificacion, c.nombres, c.apellidos, c.nit, c.dirección, c.telefono, ci.ciudad, c.fecha_nac, c.fecha_ingreso FROM clientes c INNER JOIN ciudades ci ON c.id_ciudad = ci.id INNER JOIN identificaciones i ON c.id_identificacion = i.id')
    registros = cursor.fetchall()
    return registros

def getIdentificaciones():
    cursor = conexion.cursor()
    cursor.execute('SELECT id, identificacion FROM identificaciones')
    registros = cursor.fetchall()
    return registros

def getCiudades():
    cursor = conexion.cursor()
    cursor.execute('SELECT id, ciudad FROM ciudades')
    registros = cursor.fetchall()
    return registros

def agregar_cliente(nombres, apellidos, direccion, telefono, ciudad, identificacion, nacimiento, ingreso, nit):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO clientes (nombres, apellidos, dirección, telefono, id_ciudad, id_identificacion, fecha_nac, fecha_ingreso, nit) VALUES (?,?,?,?,?,?,?,?,?)",\
        nombres, apellidos, direccion, telefono, ciudad, identificacion, nacimiento, ingreso, nit)
    conexion.commit()
    cursor.close()

def editar_cliente(nombres, apellidos, direccion, telefono, ciudad, identificacion, nacimiento, ingreso, nit, id):
    cursor = conexion.cursor()
    cursor.execute("UPDATE clientes SET nombres=?, apellidos=?, dirección=?, telefono=?, id_cuidad=?, id_identificacion=?, fecha_nac=?, fecha_ingreso=?, nit=? WHERE id=?",\
        nombres, apellidos, direccion, telefono, ciudad, identificacion, nacimiento, ingreso, nit, id)
    conexion.commit()
    cursor.close()

def eliminar_cliente(id):
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM clientes WHERE id=?", id)
    conexion.commit()
    cursor.close()