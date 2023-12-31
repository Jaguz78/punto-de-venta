import tkinter as tk
from controllers.users import *

class UserSession:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.username = None
            cls._instance.password = None
            cls._instance.role = None
            cls._instance.logged_in = False
        return cls._instance
    
    def is_logged_in(self):
        return self.logged_in

    def login(self, username, password):
        users = getUsers()
        for user in users:
            if user[0] == username and user[6] == password:
                self.username = username
                self.password = password
                self.role = user[3]
                self.logged_in = True
                success = {"success": "Login exitoso"}
                return success
        error = {"error": "Credenciales incorrectas"}
        return error

    def logout(self):
        self.username = None
        self.password = None
        self.role = None
        self.logged_in = False
        
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password

    def get_role(self):
        return self.role
    
    def changePassword(self, id, oldPass, newPass, confirmNewPass):
        users = getUsers()
        user = self.login(id, oldPass)

        if 'error' not in user:
            if newPass == confirmNewPass:
                for u in users:
                    if u[0] == id:
                        u[4] = newPass
                        changePass(id, newPass)
                        response = {"success": "Contraseña cambiada exitosamente"}
                        return response
            else:
                response = {"error": "Verifique la nueva contraseña"}
                return response
        else:
            response = {"error":"Credenciales incorrectas"}
            return response