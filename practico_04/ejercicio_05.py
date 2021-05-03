"""Base de Datos SQL - Modificación"""

import datetime
import sqlite3
from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    """Implementar la funcion actualizar_persona, que actualiza un registro de
    una persona basado en su id. Devuelve un booleano en base a si encontro el
    registro y lo actualizo o no."""

    con = sqlite3.connect("mydatabase.db")
    cursor = con.cursor()

    sentencia = "UPDATE Persona SET Nombre = ?, FechaNacimiento = ?, Dni = ?, Altura = ? WHERE IdPersona = ?"
    tdatos = (nombre, nacimiento, dni, altura, id_persona)
    cursor.execute(sentencia, tdatos)
    con.commit()

    cant = cursor.rowcount
    con.close()
    if cant == 0:
        return False
    return True

# NO MODIFICAR - INICIO


@reset_tabla
def pruebas():
    id_juan = agregar_persona(
        'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez',
                       datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (
        1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(
        1988, 4, 16), 12312312, 181) is False


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
