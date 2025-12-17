# Data Wrangling Challenge — Flujo de ensuciar y limpiar datasets

## Autor: David Mourenza Fantáns

**Resumen**:
- **Propósito**: Este repositorio muestra un flujo colaborativo: yo genero un dataset "ensuciado" a partir de [datasets/Cryptocurrency_Dataset_2023.csv](https://www.kaggle.com/datasets/iamsouravbanerjee/cryptocurrency-dataset-2021-395-types-of-crypto?select=Cryptocurrency_Dataset_2023.csv) y lo envío (por código) a un compañero; a su vez recibo un dataset ensuciado de vuelta y lo limpio por código.

**Estructura**:
- **`datasets/`**: dataset original: [Cryptocurrency_Dataset_2023.csv](https://www.kaggle.com/datasets/iamsouravbanerjee/cryptocurrency-dataset-2021-395-types-of-crypto?select=Cryptocurrency_Dataset_2023.csv).
- **`datacreator/`**: código y salida para ensuciar el dataset.
	- **Notebook**: [enshitificator.ipynb](datacreator/enshitificator.ipynb)
	- **Output**: [dirty_dataset.csv](datacreator/dirty_dataset.csv) (dataset ensuciado para enviar).
	- **Source clean**: [source_clean_dataset.csv](datacreator/source_clean_dataset.csv) (copia / referencia limpia usada antes de ensuciar).
- **`datacleaner/`**: código y resultado del proceso de limpieza.
	- **Notebook**: [cleaner.ipynb](datacleaner/cleaner.ipynb)
	- **Received**: [received_dirty_dataset.csv](datacleaner/received_dirty_dataset.csv) (dataset sucio que se recibe del compañero)
	- **Output**: [clean_dataset.csv](datacleaner/clean_dataset.csv) (resultado limpio después de procesarlo).

**Cómo usar**:
- Preparar entorno: Python 3.8+, `pandas`, `numpy`, y un servidor de Jupyter (`notebook` o `lab`).
	- Ejemplo de instalación rápida: `pip install pandas numpy jupyter`
- Para generar y enviar el dataset sucio:
	1. Abrir [datacreator/enshitificator.ipynb](datacreator/enshitificator.ipynb) y ejecutar las celdas en orden.
	2. El notebook produce `datacreator/dirty_dataset.csv` listo para compartir.
- Para recibir y limpiar el dataset sucio del compañero:
	1. Guardar el archivo recibido como [datacleaner/received_dirty_dataset.csv](datacleaner/received_dirty_dataset.csv).
	2. Abrir [datacleaner/cleaner.ipynb](datacleaner/cleaner.ipynb) y ejecutar las celdas en orden.
	3. El notebook genera `datacleaner/clean_dataset.csv` con los datos limpios.

**Notas técnicas**:
- Los notebooks usan `pandas` y `numpy` para manipulación y limpieza básica de datos.
- Diseñado para mostrar pasos reproducibles: transformación intencional de ruido (missing, outliers, formatos inconsistentes) y técnicas automáticas de limpieza.

Si quieres, puedo añadir instrucciones para crear un `requirements.txt`, scripts para automatizar (por ejemplo `make` o `python` scripts), o ejemplos de tests de calidad de datos. ¿Quieres que lo agregue? 