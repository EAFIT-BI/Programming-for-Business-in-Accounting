# -*- coding: utf-8 -*-
"""
Pruebas unitarias para el simulacro del evento evaluativo
"""

from Simulacro_evento_evaluativo import crear_dataframe
from Simulacro_evento_evaluativo import selecionar_dato

def test_crear():
    datos = crear_dataframe()
    nombres_columnas = datos.columns
    assert all(col_name in nombres_columnas for col_name in ['Nombre', 'Edad', 'Ciudad']), False
