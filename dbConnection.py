import pyodbc

def establecer_conexion():
    dsn = 'sqlServer'
    server = 'DESKTOP-L5R2EID'
    database = 'punto_de_venta'
    conexion = pyodbc.connect('DSN='+dsn+';DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database)
    return conexion
