import json
import os

ARCH_FACTURAS = os.path.join(os.path.dirname(__file__), '../bin/facturas.json')
ID_FACTURAS = os.path.join(os.path.dirname(__file__), '../bin/id_facturas.json')

def getFacturas():
    with open(ARCH_FACTURAS, 'r') as archive:
        facturas = json.load(archive)
    return facturas

def getIdFacturas():
    with open(ID_FACTURAS, 'r') as archive:
        id = json.load(archive)
    return id

def createFactura(fecha, cliente, productos, total):
    id = getIdFacturas()
    facturas = getFacturas()
    id['id'] += 1
    newFactura = {
        'id':  id['id'],
        'fecha': fecha,
        'cliente': cliente,
        'productos': productos,
        'total': total
    }
    facturas.append(newFactura)
    with open(ARCH_FACTURAS, 'w') as archive:
        json.dump(facturas, archive, indent=4)
    with open(ID_FACTURAS, 'w') as archive:
        json.dump(id, archive, indent=4)
    response = {"success": "La factura fue creada exitosamente"}
    return response