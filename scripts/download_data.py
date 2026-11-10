"""Descarga el dataset Online Retail desde el repositorio de UCI y lo deja en CSV.

Fuente: Chen, D. (2015). Online Retail [Dataset]. UCI Machine Learning Repository.
https://doi.org/10.24432/C5BW33  (licencia CC BY 4.0)

Uso:
    python scripts/download_data.py

Genera data/raw/online_retail.csv (541.909 filas, 8 columnas, unos 46 MB).
"""

from __future__ import annotations

import io
import sys
import urllib.request
import zipfile
from pathlib import Path

import pandas as pd

URL = "https://archive.ics.uci.edu/static/public/352/online+retail.zip"
EXCEL_NAME = "Online Retail.xlsx"
OUTPUT = Path(__file__).resolve().parents[1] / "data" / "raw" / "online_retail.csv"
EXPECTED_ROWS = 541_909
EXPECTED_COLUMNS = [
    "InvoiceNo",
    "StockCode",
    "Description",
    "Quantity",
    "InvoiceDate",
    "UnitPrice",
    "CustomerID",
    "Country",
]


def main() -> int:
    if OUTPUT.exists():
        print(f"Ya existe {OUTPUT}; bórralo si quieres descargarlo de nuevo.")
        return 0

    print(f"Descargando {URL} ...")
    with urllib.request.urlopen(URL, timeout=120) as response:
        archive = zipfile.ZipFile(io.BytesIO(response.read()))

    print("Convirtiendo el Excel a CSV (puede tardar un par de minutos) ...")
    with archive.open(EXCEL_NAME) as excel_file:
        df = pd.read_excel(excel_file, dtype={"InvoiceNo": str, "StockCode": str})

    if list(df.columns) != EXPECTED_COLUMNS or len(df) != EXPECTED_ROWS:
        print(
            f"El archivo descargado no tiene la forma esperada: {len(df)} filas, columnas {list(df.columns)}.",
            file=sys.stderr,
        )
        return 1

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False, encoding="utf-8")
    print(f"Listo: {OUTPUT} ({len(df):,} filas).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
