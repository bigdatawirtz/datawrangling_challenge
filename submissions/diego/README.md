# Data Wrangling Challenge

## 📋 Descripción

Este proyecto es un desafío colaborativo de limpieza de datos donde:
- **Yo creo un dataset sucio** a partir de `planets.csv` usando código de transformación
- **Envío el dataset ensuciado** a un compañero para que lo reciba
- **Recibo un dataset ensuciado** del compañero
- **Limpio los datos** con código de transformación que he desarrollado

## 🗂️ Estructura del Proyecto

```
.
├── datasets/                          # Datos originales
│   └── planets.csv                   # Dataset original limpio
│
├── datacreator/                       # Generación de datos sucios
│   ├── source_clean_dataset.csv      # Dataset limpio (entrada)
│   ├── dirty_dataset.csv             # Dataset sucio generado
│   └── enshitificator.ipynb          # Notebook: código para ensuciar datos
│
└── datacleaner/                       # Limpieza de datos
    ├── recieved_dirty_dataset.csv    # Dataset sucio recibido (entrada)
    ├── clean_dataset.csv             # Dataset limpio procesado (salida)
    └── cleaner.ipynb                 # Notebook: código para limpiar datos
```

## 🔄 Flujo del Proyecto

1. **Fase de Ensuciamiento (datacreator/)**
   - Se toma `planets.csv` como fuente llamandole `source_clean_dataset.csv`
   - El notebook `enshitificator.ipynb` aplica transformaciones para introducir errores y inconsistencias
   - Se genera `dirty_dataset.csv` para enviar al compañero

2. **Intercambio**
   - Yo envío mi dataset ensuciado al compañero
   - Recibo el dataset ensuciado del compañero (`recieved_dirty_dataset.csv`)

3. **Fase de Limpieza (datacleaner/)**
   - Se recibe `recieved_dirty_dataset.csv` del compañero
   - El notebook `cleaner.ipynb` aplica transformaciones para limpiar los datos
   - Se genera `clean_dataset.csv` con los datos procesados

## 📝 Notebooks

- **enshitificator.ipynb**: Define la estrategia de ensuciamiento de datos (valores faltantes, duplicados, formatos inconsistentes, etc.)
- **cleaner.ipynb**: Define la estrategia de limpieza de datos y restauración de consistencia

## 🎯 Objetivo

Practicar y demostrar habilidades en:
- Manipulación y transformación de datos
- Limpieza y validación de datos
- Uso de pandas/Python para data wrangling
- Documentación de procesos de datos

## 🎯 URL Datasets

- https://www.kaggle.com/datasets/fatihhazir/planets