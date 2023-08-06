import json

ARCH_USERS = '../bin/users.txts'

class User:
    def __init__(self, name, password, rol):
        self.name = name
        self.password = password
        self.rol = rol

def createUser(name, password, rol):
    users = getUsers()
    
    if any(user.name == name for user in users):
        errorMessage = {"error": "El nombre de usuario seleccionado ya existe"}
        return json.dumps(errorMessage)
    else:
        newUser = User(name, password, rol)

        with open(ARCH_USERS, '+a') as archive:
            archive.write(newUser)
        response = {"success": "El Usuario fue creado exitosamente"}
        return json.dumps(response)

def getUsers():
    with open(ARCH_USERS, 'r') as archive:
        users = archive.read()
    return users

def login(name, password):
    users = getUsers()

    for user in users:
        if user.name == name and user.password == password:
            return json.dumps(user)
        else:
            error = {"error": "Credenciales incorrectas"}
            return json.dumps(error)

def changePassword(name, oldPass, newPass, confirmNewPass):
    users = getUsers()
    user = login(name, oldPass)

    if not user.error:
        if newPass == confirmNewPass:
            for u in users:
                if u.name == user.name:
                    u.password = newPass
                    with open(ARCH_USERS, 'w') as archive:
                        archive.write(users)
                    response = {"success": "Contraseña cambiada exitosamente"}
                    json.dumps(response)
        else:
            response = {"error": "Verifique la nueva contraseña"}
            return json.dumps(response)
    else:
        response = {"error":"Credenciales incorrectas"}
        return json.dumps(response)