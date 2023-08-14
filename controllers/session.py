from controllers.users import *

class UserSession:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.username = None
            cls._instance.password = None
            cls._instance.role = None
        return cls._instance

    def login(self, username, password):
        users = getUsers()
        print(username, password)
        for user in users:
            print(user['name'], user['password'])
            if user['name'] == username and user['password'] == password:
                self.username = username
                self.password = password
                self.role = user['role']
                success = {"success": "Login exitoso"}
                return success
        error = {"error": "Credenciales incorrectas"}
        return error

    def logout(self):
        self.username = None
        self.password = None
        self.role = None

    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password

    def get_role(self):
        return self.role
    
    def changePassword(self, name, oldPass, newPass, confirmNewPass):
        users = getUsers()
        user = self.login(name, oldPass)

        if 'error' not in user:
            if newPass == confirmNewPass:
                for u in users:
                    if u['name'] == user['name']:
                        u['password'] = newPass
                        with open(ARCH_USERS, 'w') as archive:
                            json.dump(users, archive, indent=4)
                        response = {"success": "Contraseña cambiada exitosamente"}
                        return response
            else:
                response = {"error": "Verifique la nueva contraseña"}
                return response
        else:
            response = {"error":"Credenciales incorrectas"}
            return response