from dbConnection import establecer_conexion

conexion = establecer_conexion()

def getFacturas():
    cursor = conexion.cursor()
    cursor.execute('SELECT f.id, f.fecha, c.nombres, u.nombres, f.total FROM facturas f INNER JOIN clientes c ON f.id_cliente = c.id INNER JOIN usuarios u ON f.id_usuario = u.id')
    registros = cursor.fetchall()
    return registros

def getDetalle_Factura():
    cursor = conexion.cursor()
    cursor.execute('SELECT p.nombre, f.id, f.fecha, c.nombres, u.nombres, f.total from detalle_facturas df INNER JOIN productos p ON df.id_producto = p.id INNER JOIN facturas f ON df.id_factura = f.id INNER JOIN clientes c ON f.id_cliente = c.id INNER JOIN usuarios u ON f.id_usuario = u.id')
    registros = cursor.fetchall()
    return registros

def createFactura(fecha, cliente, username, productos, total):
    cursor = conexion.cursor()
    c = cursor.execute("SELECT id FROM clientes WHERE nombres = ?", cliente)
    row = c.fetchone()
    if row:
        idClient = row[0]
    else:
        idClient = None
    cursor.execute("INSERT INTO facturas (fecha, id_cliente, id_usuario, total) VALUES (?,?,?,?)",\
        fecha, idClient, username, total)
    cursor.execute("SELECT @@IDENTITY AS new_id")
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