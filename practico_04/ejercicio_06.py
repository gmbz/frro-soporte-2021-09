"""Base de Datos SQL - Creación de tablas auxiliares"""

import sqlite3
from ejercicio_01 import borrar_tabla, crear_tabla


def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    con = sqlite3.connect("mydatabase.db")
    cursor = con.cursor()

    sentencia = "CREATE TABLE IF NOT EXISTS PersonaPeso (IdPersona INTEGER, nombre TEXT(30), \
        Fecha DATETIME, Peso INTEGER, PRIMARY KEY (IdPersona, Fecha) FOREIGN KEY (IdPersona) REFERENCES Persona (IdPersona))"

    cursor.execute(sentencia)

    con.commit()

    con.close()


def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    con = sqlite3.connect("mydatabase.db")
    cursor = con.cursor()

    cursor.execute("DROP TABLE IF EXISTS PersonaPeso")
    con.commit()

    con.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
