from dbConnection import establecer_conexion

conexion = establecer_conexion()

def getFacturas():
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM facturas')
    return cursor

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
        print("No se pudo obtener el nuevo ID de la factura.")
    cursor.close()