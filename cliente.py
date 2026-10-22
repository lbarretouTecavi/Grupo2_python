"""PASO 3: un programa que CONSULTA tu propia API.

1. En una terminal levanta la API:   uvicorn app:app --reload
2. En OTRA terminal (botón + de la terminal) ejecuta:   python cliente.py
"""
import requests

URL = "http://127.0.0.1:8000"

# TODO 1: pide el resumen:  resumen = requests.get(f"{URL}/resumen", timeout=5).json()
# TODO 2: imprime cuántas ventas hay y el total en soles con print(...)
# TODO 3: pide solo las ventas en dólares:  requests.get(f"{URL}/ventas", params={"moneda": "usd"}, timeout=5).json()
#         e imprime cuántas son (len)
