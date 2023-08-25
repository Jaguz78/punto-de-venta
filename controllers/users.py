import json
import os

ARCH_USERS = os.path.join(os.path.dirname(__file__), '../bin/users.json')

def getUsers():
    with open(ARCH_USERS, 'r') as archive:
        users = json.load(archive)
    return users

def createUser(id, name, lastname, password, confirm, role):
    users = getUsers()
    idd = ""
    for user in users:
        if user['id'] == id:
            idd = "igual"
    if idd == "igual":
        errorMessage = {"error": "El id de usuario seleccionado ya existe"}
        return errorMessage
    elif password == confirm:
        newUser = {
            'id': id,
            'name': name,
            'lastname': lastname or "",
            'password': password,
            'role': role
        }
        users.append(newUser)

    with open(ARCH_USERS, 'w') as archive:
        json.dump(users, archive, indent=4)
    response = {"success": "El Usuario fue creado exitosamente"}
    return response
    
def deleteUser(id):
    users = getUsers()
    for user in users:
        if user['id'] == id:
            users.remove(user)
            with open(ARCH_USERS, 'w') as archive:
                json.dump(users, archive, indent=4)
            return {"success": "El Usuario fue eliminado exitosamente"}
                
    return {"Error": "No se encontro un usuario con ese ID"}

def editUser(id, name, lastname, role):
    users = getUsers()
    
    for user in users:
        if user['id'] == id:
            user['id'] = id
            user['name'] = name
            user['lastname'] = lastname
            user['role'] = role

            with open(ARCH_USERS, 'w') as archive:
                json.dump(users, archive, indent=4)
            return {"success": "El Usuario fue editado exitosamente"}
    return {"Error": "No existe un usuario con ese ID"}