
import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ruta = BASE_DIR / "../Datasets/F1Drivers_Dataset.csv"

datos = pd.read_csv(ruta)

"""## **Eliminación de datos**

1. **Datos faltantes**
"""

probabilidad_nan = 0.05
mascara = np.random.choice([True, False], size=datos.shape, p=[probabilidad_nan, 1 - probabilidad_nan]) # Crear una matriz de decisiones que tiene la misma forma que nuestros datos, y esas decisiones son True o False.

datos= datos.mask(mascara)

"""2. **Filas duplicadas**"""

num_filas_a_duplicar = int(datos.shape[0] * 0.2)
filas_duplicadas = datos.sample(n=num_filas_a_duplicar, replace=False) # Seleccionamos las filas que se duplicarán al azar
datos = pd.concat([datos, filas_duplicadas], ignore_index=True)

"""3. **Valores atípicos**"""

columnas_numericas = datos.select_dtypes(include=np.number).columns

probability_of_outlier = 0.05

MAGNITUD_EXTREMA = 100

df_con_outliers = datos.copy()

for col in columnas_numericas:
    #Calcular la media de la columna (para referencia)
    media = datos[col].mean()

    # Genera True donde debe ir el outlier (5% de las veces)
    mask = np.random.choice(
        [True, False],
        size=datos.shape[0], # El tamaño es el número de filas
        p=[probability_of_outlier, 1 - probability_of_outlier]
    )

    #Determinar los valores atípicos a insertar
    outlier_alto = media * MAGNITUD_EXTREMA
    #Un valor extremo bajo (ej. -100 veces la media, si es aplicable)
    outlier_bajo = media * (-MAGNITUD_EXTREMA)

    # Decidir si será alto o bajo al azar (50/50)
    valor_a_inyectar = np.random.choice([outlier_alto, outlier_bajo], size=datos.shape[0])


    # Usamos .loc para inyectar los valores solo donde la máscara es True
    # Inyectamos el valor aleatorio (alto o bajo) en las posiciones True
    df_con_outliers.loc[mask, col] = valor_a_inyectar[mask]

datos= df_con_outliers

"""4. **Inconsistencias de formato**"""

COLUMNA_A_MODIFICAR = 'Championships'
PROBABILIDAD_MODIFICACION = 0.4

# Crear la máscara booleana
mask_sep = np.random.choice(
    [True, False],
    size=datos.shape[0],
    p=[PROBABILIDAD_MODIFICACION, 1 - PROBABILIDAD_MODIFICACION]
)

# Aplicar la conversión a string y cambiar el punto por la coma
datos.loc[mask_sep, COLUMNA_A_MODIFICAR] = \
    datos.loc[mask_sep, COLUMNA_A_MODIFICAR].apply(
        lambda x: str(x).replace('.', ',')
    )

"""5. **Errores tipográficos**"""

COLUMNA_DRIVER = 'Driver'

# Lista de prefijos o sufijos que simulan errores de entrada, ortografía o etiquetas
PREFIJOS_ERROR = ["ERROR_", "FAIL_", "DATA_", "TYPO_", "WRONG_", "_MISSPELL"]

def inyectar_error_tipografico(palabra):
    if pd.isna(palabra) or len(palabra) < 3:
        return palabra

    # Elegir una posición al azar para el error
    idx = np.random.randint(0, len(palabra))

    # Elegir un carácter al azar
    nuevo_caracter = np.random.choice(list('abcdefghijklmnñopqrstuvwxyz'))

    # Construir la palabra con el error
    palabra_mutada = list(palabra)
    palabra_mutada[idx] = nuevo_caracter
    return "".join(palabra_mutada)




PROBABILIDAD_ERROR = 0.2

mask_error = np.random.choice(
    [True, False],
    size=datos.shape[0],
    p=[PROBABILIDAD_ERROR, 1 - PROBABILIDAD_ERROR]
)


datos.loc[mask_error, COLUMNA_DRIVER] = \
    datos.loc[mask_error, COLUMNA_DRIVER].apply(inyectar_error_tipografico)

"""6. **Categorías adicionales**"""

COLUMNAS_CATEGORICAS = ['Nationality', 'Championship Years', 'Decade', 'Active', 'Champion']

CATEGORIAS_INUSUALES = [
    "UNKNOWN_VALUE",
    "N/A_INPUT",
    "INVALID_ENTRY",
    "Z_OUTLIER",
    "ERROR_CHECK"
]

PROBABILIDAD_INYECCION = 0.05

def inyectar_categoria_inusual(valor_original):
    # Usamos np.random.choice para elegir una categoría de la lista
    return np.random.choice(CATEGORIAS_INUSUALES)


for columna in COLUMNAS_CATEGORICAS:
    mask_adicional = np.random.choice(
        [True, False],
        size=datos.shape[0],
        p=[PROBABILIDAD_INYECCION, 1 - PROBABILIDAD_INYECCION]
    )


    datos.loc[mask_adicional, columna] = \
        datos.loc[mask_adicional, columna].apply(inyectar_categoria_inusual)

"""7. **Tipos de datos incorrectos**"""

COLUMNA_ACTIVA = 'Race_Starts'

datos[COLUMNA_ACTIVA] = datos[COLUMNA_ACTIVA].astype(str)

"""9. **Encabezados incorrectos**"""

columnas_originales = datos.columns.tolist()


mapeo_errores = {

    'Points': 'Puntos$$',
    'Championships': 'cHaMpIoNsHiPs',
}


datos.rename(columns=mapeo_errores, inplace=True)

"""10. **Símbolos de puntuación extra (1000 € )**"""

COLUMNA_ACTIVA = 'Race_Wins'

SIMBOLOS_EXTRA = ["€", "$"]

PROBABILIDAD_INYECCION = 0.08


def inyectar_simbolos_extra(valor_original):
    # Manejar NaN/valores nulos para que no falle la conversión a string
    if pd.isna(valor_original):
        return valor_original

    # Convertir a string para poder manipular el texto
    valor_str = str(valor_original)

    # Elegir un símbolo al azar
    simbolo = np.random.choice(SIMBOLOS_EXTRA)

    return valor_str + simbolo


# Asumiendo que tu DataFrame se llama 'datos'
df_con_simbolos = datos.copy()

    # 1. Crear la máscara booleana específica para la columna
mask_simbolos = np.random.choice(
    [True, False],
    size=df_con_simbolos.shape[0],
    p=[PROBABILIDAD_INYECCION, 1 - PROBABILIDAD_INYECCION]
)

    # 2. Aplicar la función de inyección solo a las filas seleccionadas (usando .loc)
df_con_simbolos.loc[mask_simbolos, COLUMNA_ACTIVA] = \
    df_con_simbolos.loc[mask_simbolos, COLUMNA_ACTIVA].apply(inyectar_simbolos_extra)

"""8. **No hay codificación**"""

datos.to_csv('DatosSucios.csv', encoding='latin-1', index=False, errors='ignore')