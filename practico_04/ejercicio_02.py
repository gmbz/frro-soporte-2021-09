"""Base de Datos SQL - Alta"""
import sqlite3
import datetime
from ejercicio_01 import reset_tabla


def agregar_persona(nombre, nacimiento, dni, altura):
    """Implementar la funcion agregar_persona, que inserte un registro en la 
    tabla Persona y devuelva los datos ingresados el id del nuevo registro."""
    con = sqlite3.connect("mydatabase.db")
    cursor = con.cursor()
                            
    sentencia = "INSERT INTO Persona VALUES (null, ?, ?, ?, ?)"
    tdatos = (nombre, nacimiento, dni, altura)
    cursor.execute(sentencia, tdatos)
    con.commit()
    last_id = cursor.lastrowid      # https://docs.python.org/es/3.9/library/sqlite3.html#sqlite3.Cursor.lastrowid
    con.close()
    return last_id


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
