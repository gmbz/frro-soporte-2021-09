"""Base de Datos SQL - Búsqueda"""

import datetime
import sqlite3
from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    """Implementar la funcion buscar_persona, que devuelve el registro de una 
    persona basado en su id. El return es una tupla que contiene sus campos: 
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro, 
    devuelve False."""
    con = sqlite3.connect("mydatabase.db")
    cursor = con.cursor()
                            
    sentencia = "SELECT * FROM Persona WHERE IdPersona = ?"
    cursor.execute(sentencia, (id_persona,))

    persona = cursor.fetchone()  # fetchone obtiene la siguiente fila
    con.close()
    if persona is None:
        return False
    lista = list(persona)
    formato = "%Y-%m-%d %H:%M:%S"
    objeto_datetime = datetime.datetime.strptime(lista[2],formato)
    lista[2] = objeto_datetime
    persona = tuple(lista)
    return tuple(persona)


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
