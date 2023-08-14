import json
import os

ARCH_USERS = os.path.join(os.path.dirname(__file__), '../bin/users.json')

def createUser(name, password, role):
    users = getUsers()
    
    for user in users:
        if user['name'] == name:
            errorMessage = {"error": "El nombre de usuario seleccionado ya existe"}
            return errorMessage
    else:
        newUser = {
            'name': name,
            'password': password,
            'role': role
        }
        users.append(newUser)

        with open(ARCH_USERS, 'w') as archive:
            json.dump(users, archive, indent=4)
        response = {"success": "El Usuario fue creado exitosamente"}
        return response

def getUsers():
    with open(ARCH_USERS, 'r') as archive:
        users = json.load(archive)
    return users