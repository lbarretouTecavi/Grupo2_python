"""PASO 2: tu API.   Levantar:  uvicorn app:app --reload     y abrir  /docs  en el navegador

Antes de este paso debes haber ejecutado proyecto.py (crea la carpeta salida/).
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


@app.get("/ventas")
def listar(moneda: str | None = None):
    # TODO 1: si moneda es None devuelve toda la lista;
    #         si no, devuelve solo los elementos cuyo campo "moneda" coincide
    #         (para moneda compara con moneda.upper(), así "usd" también funciona)
    pass


@app.get("/ventas/{venta_id}")
def detalle(venta_id: int):
    # TODO 2: busca el elemento cuyo "id" sea igual a venta_id y devuélvelo.
    #         Si no existe: raise HTTPException(status_code=404, detail="Venta no encontrada")
    pass


@app.get("/resumen")
def resumen():
    # TODO 3: devuelve resumir(ventas)
    pass
