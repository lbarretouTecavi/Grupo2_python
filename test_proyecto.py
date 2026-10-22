"""PASO 4: pruebas.  Ejecuta:  pytest -v"""
import pandas as pd
from fastapi.testclient import TestClient

from app import app
from proyecto import convertir_a_soles, limpiar_ventas


def test_diez_dolares_son_37_soles():             # <- ESTA YA ESTA RESUELTA: sirve de ejemplo
    assert convertir_a_soles(10, "USD") == 37.0


def test_moneda_se_normaliza_y_monto_vacio_se_rechaza():
    # TODO: arma una tabla chica:
    #   df = pd.DataFrame([{"id": "1", "producto": "Mouse", "monto": "10", "moneda": " usd "},
    #                      {"id": "2", "producto": "Mouse", "monto": "", "moneda": "PEN"}])
    #   buenas, rechazadas = limpiar_ventas(df)
    # y comprueba: la moneda de la venta buena es "USD" y el motivo de la rechazada es "monto_invalido"
    pass


def test_venta_inexistente_da_404():
    # TODO: TestClient(app).get("/ventas/999") y comprueba que status_code == 404
    pass
