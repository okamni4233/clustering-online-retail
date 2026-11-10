# Segmentación de clientes con RFM y K-Means

> **English summary.** Customer segmentation of a UK online retailer (UCI Online Retail dataset, 541,909 transaction lines, Dec 2010 – Dec 2011). Transactions are aggregated into Recency, Frequency and Monetary features for 4,338 customers, log-transformed, scaled and clustered with K-Means. Four segments are kept for interpretability (silhouette 0.337), even though k = 2 has the highest silhouette (0.433).

## Qué hace

El notebook `notebooks/customer_segmentation_kmeans.ipynb`:

1. limpia las transacciones (sin cliente, canceladas, con cantidad o precio no positivos): de 541.909 líneas quedan 397.884;
2. construye las variables RFM por cliente (4.338 clientes): días desde la última compra, número de facturas y gasto total;
3. aplica logaritmo y estandarización, y compara K-Means de k = 2 a k = 10 con el método del codo y el Silhouette Score;
4. segmenta con k = 4 y describe cada segmento.

## Resultados

**El 16,5 % de los clientes genera el 64,9 % del ingreso.** La segmentación separa ese grupo de otros tres con comportamientos distintos:

| Segmento | Clientes | % de clientes | % del ingreso | Recencia mediana (días) | Frecuencia mediana (facturas) | Acción propuesta |
|---|---|---|---|---|---|---|
| Clientes VIP | 716 | 16,5 | 64,9 | 8 | 10 | Retención prioritaria, sin descuentos generales |
| Regulares o potencialmente leales | 1.173 | 27,0 | 23,7 | 56 | 4 | Aumentar la frecuencia de compra |
| Recientes de bajo valor | 837 | 19,3 | 5,2 | 17 | 2 | Conseguir la segunda y tercera compra |
| En riesgo | 1.612 | 37,2 | 6,2 | 177 | 1 | Reactivación de bajo costo |

**Elección de k.** Silhouette: 0,4329 (k = 2), 0,3365 (k = 3), 0,3371 (k = 4), 0,3161 (k = 5). Se elige k = 4 por interpretabilidad: k = 2 separa mejor, pero es demasiado grueso para definir acciones distintas.

**Estabilidad.** Al repetir K-Means con 20 semillas, la partición con k = 4 coincide con la de referencia con un índice de Rand ajustado medio de 0,971 (mínimo 0,942). Sobre 20 submuestras del 80 % de los clientes, la media es 0,950 (mínimo 0,819). Con k = 5 la estabilidad cae a 0,878 de media en submuestras.

## Limitaciones

- Un silhouette de 0,34 indica separación moderada: los segmentos son reproducibles, pero sus fronteras son difusas.
- Las acciones propuestas son hipótesis a partir del perfil RFM. El dataset no trae campañas ni costos, así que su efecto no se puede medir aquí.
- Se excluye el 24,9 % de las líneas por no tener identificador de cliente.
- La recencia se mide respecto de la última fecha del dataset (diciembre de 2011) y el periodo cubre un solo año, por lo que no se distingue estacionalidad de abandono.

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
