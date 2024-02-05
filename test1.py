# -*- coding: utf-8 -*-
"""
Pruebas unitarias para el simulacro del evento evaluativo
"""

from simulacro import crear


def test_crear():
    datos = crear()
    nombres_columnas = datos.columns
    assert all(col_name in nombres_columnas for col_name in [
               'Nombre', 'Edad', 'Ciudad']), False
