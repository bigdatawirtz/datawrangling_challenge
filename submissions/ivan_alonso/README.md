# Data Cleaning & Preprocessing Challenge

## Descripción del Proyecto

Este repositorio contiene el trabajo realizado para la práctica de **Limpieza y Preprocesamiento de Datos**. El objetivo es simular escenarios del mundo real donde los datos crudos rara vez son perfectos.

Se ha trabajado sobre dos datasets distintos: **Amazon** y **Spotify**.

---

## Flujo de Trabajo

### 1. Fase de "Ensuciado" (Data Creator)
Utilizando **Python**, se modificaron datasets limpios para introducir **al menos 10 tipos de errores** y anomalías, incluyendo:
* Inconsistencias de formatos (fechas, números).
* Errores de codificación (guardado en `cp1252`).
* Inyección de nulos, duplicados y outliers.
* Errores tipográficos y categorías basura.
* Encabezados sucios y tipos de datos incorrectos.

*El reporte detallado de los errores introducidos se encuentra al final de cada cuaderno de "Ensuciar".*

### 2. Fase de Limpieza y Análisis (Data Cleaner)
Se procedió a recuperar la calidad del dato mediante:
* Carga correcta de archivos con codificación no estándar.
* Limpieza con Regex y estandarización de columnas.
* Imputación de nulos y manejo de outliers.

Posteriormente, se realizó un **Análisis Exploratorio (EDA)** con estadísticas y visualizaciones (Seaborn/Matplotlib).

*El reporte de limpieza y hallazgos se encuentra al final de cada cuaderno de "Limpiar".*

---

## Contenido del Repositorio

El proyecto se divide en dos flujos independientes (uno por dataset):

### Dataset Amazon
* `ensuciar_dataset_amazon.ipynb`: Script que genera errores y exporta el CSV sucio. Incluye reporte de generación.
* `limpiar_dataset_amazon.ipynb`: Script que limpia los datos, genera visualizaciones y exporta el CSV limpio. Incluye reporte de análisis.

### Dataset Spotify
* `ensuciar_dataset_spotify.ipynb`: Script que genera errores y exporta el CSV sucio. Incluye reporte de generación.
* `limpiar_dataset_spotify.ipynb`: Script que limpia los datos, genera visualizaciones y exporta el CSV limpio. Incluye reporte de análisis.
