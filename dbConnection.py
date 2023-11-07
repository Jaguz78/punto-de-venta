import pyodbc

def establecer_conexion():
    servidor = 'Mani'
    bd = 'punto_de_venta'
    usuario = 'sa'
    contra = 'Gonzalez0320'
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+servidor+';DATABASE='+bd+';UID='+usuario+';PWD='+contra)
    return conexion
