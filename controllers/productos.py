import json
import os

ARCH_PRODUCTOS = os.path.join(os.path.dirname(__file__), '../bin/productos.json')

def getProductos():
    with open(ARCH_PRODUCTOS, 'r') as archive:
        productos = json.load(archive)
    return productos

def agregar_producto(id, nombre, precio, iva, nota):
    productos = getProductos()
    idd = ""
    for p in productos:
        if p['id'] == id:
            idd = "igual"
    if idd == "igual":
        errorMessage = {"Error": "El Id del Producto ya existe"}
        return errorMessage
    else:
        nuevo = {
            'id' : id,
            'nombre' : nombre,
            'precio' : precio,
            'iva' : iva,
            'nota' : nota
        }
        productos.append(nuevo)

    with open(ARCH_PRODUCTOS, 'w') as archive:
        json.dump(productos, archive, indent=4)
    response = {"success": "El Producto fue agregado exitosamente"}
    return response

def editar_producto(id, nombre, precio, iva, nota):
    productos = getProductos()
    
    for p in productos:
        if p['id'] == id:
            p['id'] = id
            p['nombre'] = nombre
            p['precio'] = precio
            p['iva'] = iva
            p['nota'] = nota

            with open(ARCH_PRODUCTOS, 'w') as archive:
                json.dump(productos, archive, indent=4)
            return {"success": "El Producto fue editado exitosamente"}
        
    return {"Error": "No existe un Producto con ese Id"}

def eliminar_producto(id):
    productos = getProductos()
    for p in productos:
        if p['id'] == id:
            productos.remove(p)
            with open(ARCH_PRODUCTOS, 'w') as archive:
                json.dump(productos, archive, indent=4)
            return {"success": "El Producto fue eliminado exitosamente"}
                        
    return {"Error": "No se encontro un Producto con ese Id"}