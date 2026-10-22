"""Caso 2 - Tienda online.   PASO 1: pasar todas las ventas a soles.

Cómo se usa:  python proyecto.py --entrada datos/ventas.csv
Busca los  # TODO  y complétalos uno por uno. Después de cada uno, ejecuta y mira qué pasa.
"""
import argparse
import json
from pathlib import Path

import pandas as pd

TASAS = {"PEN": 1.0, "USD": 3.70, "EUR": 4.00}     # cuántos soles vale 1 unidad de cada moneda


def convertir_a_soles(monto, moneda):
    # TODO 1: devuelve monto * TASAS[moneda] redondeado a 2 decimales
    pass


def limpiar_ventas(df):
    """Recibe la tabla leída del CSV (todo texto) y devuelve (ventas_buenas, ventas_rechazadas)."""
    buenas, rechazadas = [], []
    for fila in df.to_dict("records"):
        # TODO 2: normaliza la moneda: fila["moneda"].strip().upper()
        # TODO 3: convierte fila["monto"] a float dentro de un try/except ValueError.
        #         Si falla, o si el monto es 0 o negativo -> rechazadas.append({**fila, "motivo": "monto_invalido"}) y continue
        # TODO 4: si la moneda no está en TASAS -> rechazadas.append({**fila, "motivo": "moneda_invalida"}) y continue
        # TODO 5: si todo está bien, agrega a buenas un diccionario con
        #         id (int), producto, monto, moneda y monto_pen (convertir_a_soles)
        pass
    return buenas, rechazadas


def resumir(ventas):
    """Devuelve {"ventas": cuántas, "total_pen": suma de monto_pen (2 decimales)}."""
    # TODO 6
    pass


def main():
    parser = argparse.ArgumentParser(description="Ventas convertidas a soles")
    parser.add_argument("--entrada", default="datos/ventas.csv")
    parser.add_argument("--salida", default="salida")
    args = parser.parse_args()

    df = pd.read_csv(args.entrada, dtype=str, keep_default_na=False)    # dtype=str: todo llega como texto
    buenas, rechazadas = limpiar_ventas(df)
    salida = Path(args.salida)
    salida.mkdir(exist_ok=True)
    pd.DataFrame(buenas).to_csv(salida / "ventas.csv", index=False)
    pd.DataFrame(rechazadas).to_csv(salida / "rechazadas.csv", index=False)
    (salida / "resumen.json").write_text(json.dumps(resumir(buenas), indent=2), encoding="utf-8")
    print(f"{len(buenas)} ventas, {len(rechazadas)} rechazadas -> {salida}/")


if __name__ == "__main__":
    main()
