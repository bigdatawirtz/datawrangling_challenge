# 📚 README: Tarea de Limpieza y Preprocesamiento de Datos (Data Wrangling Challenge) Gabriel Tenreiro Calvo

Este repositorio contiene la solución completa para el desafío de **Limpieza y Preprocesamiento de Datos (Data Wrangling)**. El proyecto simula el ciclo completo de la calidad de los datos, desde la creación intencionada de errores hasta su corrección y análisis.

La tarea se ejecutó asumiendo dos roles distintos:
* **Data Creator:** Creación de un dataset sucio basado en datos de **Viviendas (Housing Data)**.
* **Data Cleaner:** Limpieza, preprocesamiento y análisis de un dataset sucio de **Ventas de Videojuegos** recibido.

## 🚀 Estructura del Repositorio

La organización del repositorio sigue la estructura estándar para este tipo de desafío:

```text
.
├── datacleaner/
│   ├── clean_dataset.csv           # ⬅️ Dataset de Videojuegos limpiado (202 filas)
│   ├── cleaner.ipynb               # ⬅️ Notebook con la lógica de limpieza y el análisis exploratorio
│   └── recieved_dirty_dataset.csv  # ⬅️ Dataset sucio de Videojuegos recibido
└── datacreator/
    ├── dirty_dataset.csv           # ⬅️ Dataset sucio de Viviendas creado con 10 errores
    ├── enshitificator.ipynb        # ⬅️ Notebook que documenta la inyección de errores en Viviendas
    └── source_clean_dataset.csv    # ⬅️ Dataset original de Viviendas (base de partida)

    I. Rol: Data Creator (Creación de Dataset Sucio)
Dataset Original: Base de datos de Ventas de Viviendas (Housing Data). Dataset Modificado: Muestra aleatoria modificada con 10 tipos de errores.



    II. Rol: Data Cleaner (Limpieza y Análisis)
"

