import json
import os

ARCH_CLIENTES = os.path.join(os.path.dirname(__file__), '../bin/clientes.json')

def getClientes():
    with open(ARCH_CLIENTES, 'r') as archive:
        clientes = json.load(archive)
    return clientes

def agregar_cliente(id, identificacion, nombres, apellidos, direccion, telefono, ciudad, nacimiento, ingreso):
    clientes = getClientes()
    idd = ""
    for c in clientes:
        if c['id'] == id:
            idd = "igual"
    if idd == "igual":
        errorMessage = {"Error": "El Id del Cliente ya existe"}
        return errorMessage
    else:
        nuevo = {
            'id' : id,
            'identificacion' : identificacion,
            'nombres' : nombres,
            'apellidos' : apellidos,
            'direccion' : direccion,
            'telefono' : telefono,
            'ciudad' : ciudad,
            'nacimiento' : nacimiento,
            'ingreso' : ingreso
        }
        clientes.append(nuevo)

    with open(ARCH_CLIENTES, 'w') as archive:
        json.dump(clientes, archive, indent=4)
    response = {"success": "El Cliente fue agregado exitosamente"}
    return response

def editar_cliente(id, identificacion, nombres, apellidos, direccion, telefono, ciudad, nacimiento, ingreso):
    clientes = getClientes()
    
    for c in clientes:
        if c['id'] == id:
            c['id'] = id
            c['identificacion'] = identificacion
            c['nombres'] = nombres
            c['apellidos'] = apellidos
            c['direccion'] = direccion
            c['telefono'] = telefono
            c['ciudad'] = ciudad
            c['nacimiento'] = nacimiento
            c['ingreso'] = ingreso

            with open(ARCH_CLIENTES, 'w') as archive:
                json.dump(clientes, archive, indent=4)
            return {"success": "El Cliente fue editado exitosamente"}
    return {"Error": "No existe un Cliente con ese Id"}

def eliminar_cliente(id):
    clientes = getClientes()
    for c in clientes:
        if c['id'] == id:
            clientes.remove(c)
            with open(ARCH_CLIENTES, 'w') as archive:
                json.dump(clientes, archive, indent=4)
            return {"success": "El Cliente fue eliminado exitosamente"}                
    return {"Error": "No se encontro un Cliente con ese Id"}