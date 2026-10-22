"""
Caso 2 - Tienda online.
PASO 1: Pasar todas las ventas a soles.

Cómo se usa:
    python proyecto.py --entrada datos/ventas.csv

Busca los # TODO y complétalos uno por uno.
Después de cada uno, ejecuta y observa qué sucede.
"""

import argparse
import json
from pathlib import Path

import pandas as pd

# Cuántos soles vale una unidad de cada moneda
TASAS = {
    "PEN": 1.0,
    "USD": 3.70,
    "EUR": 4.00,
}


def convertir_a_soles(monto, moneda):
    """Convierte un monto a soles y lo redondea a dos decimales."""
    return round(monto * TASAS[moneda], 2)


def limpiar_ventas(df):
    """
    Recibe la tabla leída del CSV (todo texto)
    y devuelve (ventas_buenas, ventas_rechazadas).
    """
    buenas, rechazadas = [], []

    for fila in df.to_dict("records"):
        # TODO 2: normalizar moneda
        moneda = fila["moneda"].strip().upper()

        # TODO 3: convertir y validar monto
        try:
            monto = float(fila["monto"].strip())

            # Evitar valores infinitos o NaN
            if not pd.notna(monto) or monto <= 0 or monto == float("inf") or monto == float("-inf"):
                raise ValueError

        except (ValueError, AttributeError):
            rechazadas.append({
                **fila,
                "motivo": "monto_invalido",
            })
            continue

        # TODO 4: validar moneda
        if moneda not in TASAS:
            rechazadas.append({
                **fila,
                "motivo": "moneda_invalida",
            })
            continue

        # TODO 5: agregar venta válida
        buenas.append({
            "id": int(fila["id"]),
            "producto": fila["producto"],
            "monto": monto,
            "moneda": moneda,
            "monto_pen": convertir_a_soles(monto, moneda),
        })

    return buenas, rechazadas


def resumir(ventas):
    # TODO 6: contar ventas y sumar sus importes en soles
    return {
        "ventas": len(ventas),
        "total_pen": round(
            sum(venta["monto_pen"] for venta in ventas),
            2,
        ),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Ventas convertidas a soles"
    )
    parser.add_argument(
        "--entrada",
        default="datos/ventas.csv",
    )
    parser.add_argument(
        "--salida",
        default="salida",
    )
    args = parser.parse_args()

    df = pd.read_csv(
        args.entrada,
        dtype=str,
        keep_default_na=False,
    )

    buenas, rechazadas = limpiar_ventas(df)

    salida = Path(args.salida)
    salida.mkdir(parents=True, exist_ok=True)

    pd.DataFrame(buenas).to_csv(
        salida / "ventas.csv",
        index=False,
    )

    pd.DataFrame(rechazadas).to_csv(
        salida / "rechazadas.csv",
        index=False,
    )

    (salida / "resumen.json").write_text(
        json.dumps(resumir(buenas), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(
        f"{len(buenas)} ventas, "
        f"{len(rechazadas)} rechazadas -> {salida}/"
    )


if __name__ == "__main__":
    main()