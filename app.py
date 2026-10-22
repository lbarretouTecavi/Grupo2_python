
"""PASO 2: tu API.

Levantar: uvicorn app:app --reload
Abrir: http://127.0.0.1:8000/docs

Antes de este paso debes haber ejecutado proyecto.py
(crea la carpeta salida/).
"""

from pathlib import Path

import pandas as pd
from fastapi import FastAPI, HTTPException

from proyecto import resumir

app = FastAPI(title="Tienda online")
RUTA = Path("salida/ventas.csv")


def cargar():
    if not RUTA.exists():
        return []
    return pd.read_csv(RUTA).to_dict("records")


ventas = cargar()


# TODO 1: Listar todas las ventas o filtrar por moneda
@app.get("/ventas")
def listar(moneda: str | None = None):
    if moneda is None:
        return ventas

    return [venta for venta in ventas if venta["moneda"] == moneda.upper()]


# TODO 2: Buscar una venta por su ID
@app.get("/ventas/{venta_id}")
def detalle(venta_id: int):
    for venta in ventas:
        if venta["id"] == venta_id:
            return venta

    raise HTTPException(status_code = 404, detail = "Venta no encontrada")


# TODO 3: Obtener el resumen de las ventas
@app.get("/resumen")
def resumen():
    return resumir(ventas)
