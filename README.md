# Segmentación de clientes con RFM y K-Means

> **English summary.** Customer segmentation of a UK online retailer (UCI Online Retail dataset, 541,909 transaction lines, Dec 2010 – Dec 2011). Transactions are aggregated into Recency, Frequency and Monetary features for 4,338 customers, log-transformed, scaled and clustered with K-Means. Four segments are kept for interpretability (silhouette 0.337), even though k = 2 has the highest silhouette (0.433).

## Qué hace

El notebook `notebooks/customer_segmentation_kmeans.ipynb`:

1. limpia las transacciones (sin cliente, canceladas, con cantidad o precio no positivos): de 541.909 líneas quedan 397.884;
2. construye las variables RFM por cliente (4.338 clientes): días desde la última compra, número de facturas y gasto total;
3. aplica logaritmo y estandarización, y compara K-Means de k = 2 a k = 10 con el método del codo y el Silhouette Score;
4. segmenta con k = 4 y describe cada segmento.

## Resultados

Silhouette por número de clústeres: 0,4329 (k = 2), 0,3365 (k = 3), 0,3371 (k = 4), 0,3161 (k = 5). Se elige k = 4 por interpretabilidad: k = 2 separa mejor, pero es demasiado grueso para definir acciones distintas.

| Segmento | Clientes | Recencia media (días) | Frecuencia media (facturas) | Gasto medio (£) |
|---|---|---|---|---|
| Clientes VIP | 716 | 12,1 | 13,7 | 8.074,27 |
| Regulares o potencialmente leales | 1.173 | 71,1 | 4,1 | 1.802,83 |
| Recientes de bajo valor | 837 | 18,1 | 2,2 | 551,82 |
| En riesgo | 1.612 | 182,5 | 1,3 | 343,45 |

## Limitaciones

- Un silhouette de 0,34 indica separación moderada: los segmentos son cortes sobre un continuo, no grupos claramente aislados.
- No se evaluó la estabilidad de los segmentos (otras semillas, submuestras) ni se validaron con una campaña real.
- Los promedios de gasto son sensibles a valores extremos (hay clientes con compras muy grandes).
- Se excluye el 24,9 % de las líneas por no tener identificador de cliente.

## Cómo reproducirlo

```bash
pip install -r requirements.txt
python scripts/download_data.py
jupyter nbconvert --to notebook --execute --inplace notebooks/customer_segmentation_kmeans.ipynb
```

Probado con Python 3.13. El notebook deja `customer_segments.csv` y `rfm_table.csv` en `data/processed/`.

## Datos

El dataset no se versiona (46 MB). `scripts/download_data.py` lo descarga del repositorio de UCI y lo convierte a CSV.

Fuente: Chen, D. (2015). *Online Retail* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33 (licencia CC BY 4.0).

## Estructura

```
data/
  raw/          dataset descargado (no versionado)
  processed/    salidas del notebook (no versionadas)
notebooks/
  customer_segmentation_kmeans.ipynb
scripts/
  download_data.py
requirements.txt
```
