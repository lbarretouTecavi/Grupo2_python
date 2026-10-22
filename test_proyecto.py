"""PASO 4: Pruebas automatizadas.

Ejecutar: python -m pytest -v
"""

import pandas as pd
from fastapi.testclient import TestClient

from app import app
from proyecto import convertir_a_soles, limpiar_ventas


# PRUEBA 1: Verificar la conversion de dolares a soles
def test_diez_dolares_son_37_soles():
    assert convertir_a_soles(10, "USD") == 37.0


# PRUEBA 2: Verificar la normalizacion de moneda
# y el rechazo de montos vacios
def test_moneda_se_normaliza_y_monto_vacio_se_rechaza():

    # Crear datos de prueba
    df = pd.DataFrame([
        {
            "id": "1",
            "producto": "Mouse",
            "monto": "10",
            "moneda": " usd "
        },
        {
            "id": "2",
            "producto": "Mouse",
            "monto": "",
            "moneda": "PEN"
        }
    ])

    # Ejecutar la funcion de limpieza
    buenas, rechazadas = limpiar_ventas(df)

    # Verificar que exista una venta valida
    assert len(buenas) == 1

    # Verificar que la moneda se normalizo a USD
    assert buenas[0]["moneda"] == "USD"

    # Verificar que exista una venta rechazada
    assert len(rechazadas) == 1

    # Verificar el motivo del rechazo
    assert rechazadas[0]["motivo"] == "monto_invalido"


# PRUEBA 3: Verificar que una venta inexistente
# devuelva el codigo HTTP 404
def test_venta_inexistente_da_404():

    # Crear cliente de pruebas de FastAPI
    client = TestClient(app)

    # Consultar una venta inexistente
    response = client.get("/ventas/999")

    # Verificar el codigo de respuesta
    assert response.status_code == 404