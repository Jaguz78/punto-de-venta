from dbConnection import establecer_conexion

conexion = establecer_conexion()

def getFacturas():
    cursor = conexion.cursor()
    cursor.execute('SELECT f.id, f.fecha, c.nombres, u.nombres, f.total FROM facturas f INNER JOIN clientes c ON f.id_cliente = c.id INNER JOIN usuarios u ON f.id_usuario = u.id')
    registros = cursor.fetchall()
    return registros

def getDetalle_Factura():
    cursor = conexion.cursor()
    cursor.execute('SELECT f.id, f.fecha, c.nombres, u.nombres, f.total, p.nombre  FROM detalle_facturas df INNER JOIN productos p ON df.id_producto = p.id INNER JOIN facturas f ON df.id_factura = f.id INNER JOIN clientes c ON f.id_cliente = c.id INNER JOIN usuarios u ON f.id_usuario = u.id')
    registros = cursor.fetchall()
    return registros

def getProductos_Factura(id):
    cursor = conexion.cursor()
    cursor.execute('SELECT p.nombre, df.cantidad FROM detalle_facturas df INNER JOIN productos p ON df.id_producto = p.id WHERE df.id_factura = ?', id)
    registros = cursor.fetchall()
    return registros

def createFactura(fecha, cliente, session, productos):
    cursor = conexion.cursor()
    c = cursor.execute("SELECT id FROM clientes WHERE nombres = ?", cliente)
    conexion.commit()
    row = c.fetchone()
    if row:
        idClient = row[0]
    else:
        idClient = None
    cursor.execute("INSERT INTO facturas (fecha, id_cliente, id_usuario) VALUES (?,?,?)",\
        fecha, idClient, session.username)
    conexion.commit()
    cursor.execute("SELECT SCOPE_IDENTITY() AS new_id")
    conexion.commit()
    row = cursor.fetchone()
    if row:
        new_id = row.new_id
        for p in productos:
            cursor.execute("INSERT INTO detalle_facturas (id_factura, id_producto, cantidad, subtotal) VALUES (?,?,?,?)",\
                           new_id, p[0], p[1], p[2])
            conexion.commit()
    else:
        print("No se pudo obtener el nuevo ID de la factura")
    cursor.close()