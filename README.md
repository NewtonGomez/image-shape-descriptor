# Análisis de Momentos de Imagen e Invariantes de Hu

## Descripción General

Este repositorio contiene un sistema de análisis de imágenes que implementa técnicas de visión computacional para extraer características invariantes de formas binarias. El proyecto calcula **momentos centrales** e **invariantes de Hu** en imágenes, evaluando su robustez ante transformaciones geométricas como rotación, traslación y escalado.

Es un trabajo académico para la materia **Nuevos Paradigmas Tecnológicos** del programa de Posgrado.

Las imagenes fueron obtenidas del repositorio: Ralph, R. (s. f.). MPEG-7 Shape Database. DABI Lab - Temple University. https://dabi.temple.edu/external/shape/MPEG7/dataset.html

## Objetivos

- Extraer características de formas mediante momentos de imagen
- Calcular invariantes de Hu (descriptores de forma invariantes a transformaciones)
- Evaluar la invariancia de las características ante:
  - Rotación
  - Traslación
  - Escalado
- Analizar componentes conectados y contornos de objetos
- Generar un conjunto de datos con características para análisis posterior

## 📁 Estructura del Proyecto

```
├── main.py                      # Script principal que orquesta el análisis
├── image_moments.py             # Cálculo de momentos centrales e invariantes de Hu
├── image_transformations.py     # Transformaciones geométricas (rotación, traslación, escalado)
├── tools.py                     # Funciones auxiliares y procesamiento de imágenes
├── Resultados_2D.csv            # Archivo de salida con los resultados del análisis
├── samples/                     # Imágenes de entrada para procesar
├── data/                        # Datos de transformaciones aplicadas
│   ├── originals/               # Imágenes originales en formato CSV
│   ├── rotated/                 # Imágenes rotadas en formato CSV
│   ├── translated/              # Imágenes trasladadas en formato CSV
│   ├── scalated/                # Imágenes escaladas en formato CSV
├── graphs/                      # Visualización de las transformaciones.
```

## Módulos Principales

### `main.py`
Script principal que:
1. Carga imágenes del carpeta `samples`
2. Las binariza con un umbral de 128
3. Calcula momentos centrales para la imagen original
4. Calcula invariantes de Hu
5. Aplica transformaciones (traslación, rotación, escalado)
6. Analiza componentes conectados (4-conectado y 8-conectado)
7. Encuentra contornos
8. Exporta todos los resultados a `Resultados_2D.csv`

### `image_moments.py`
Implementa el cálculo de momentos de imagen:

- **Momentos centrales (μ)**: Momentos calculados respecto al centroide
  - `m00`: Área total (suma de píxeles)
  - `m10`, `m01`: Componentes del centroide
  
- **Momentos normalizados (η)**: Momentos centrales normalizados por área
  - `eta_pq`: Momento central normalizado de orden (p,q)
  
- **Invariantes de Hu (h₁-h₇)**: 7 descriptores invariantes a transformaciones afines
  - Robustos contra rotación, escalado y reflexión

### `image_transformations.py`
Implementa transformaciones geométricas:

- **`rotate_image()`**: Rotación de imagen alrededor del centroide
- **`translate_image()`**: Traslación de píxeles
- **`scalate_image()`**: Escalado proporcional

### `tools.py`
Funciones auxiliares:

- **`process_and_binarize()`**: Carga imagen y la convierte a binaria
- **`connected_components()`**: Cuenta componentes conectados (4 u 8 vecindad)
- **`find_outline()`**: Detecta el contorno de objetos
- **`save_matrix_to_csv()`**: Exporta matrices a formato CSV

##  Datos de Salida

El archivo `Resultados_2D.csv` contiene las siguientes características por imagen:

### Columnas de la imagen original:
- `Imagen`: Nombre del archivo
- `Area`: Momento m₀₀ (área total)
- `N4`: Componentes conectados (4-conectado)
- `N8`: Componentes conectados (8-conectado)
- `Contorno_Perimetro`: Perímetro del contorno
- `m00`, `centroid`: Momento de área y centroide
- `eta_00` a `eta_30`: Momentos normalizados
- `h1` a `h7`: Invariantes de Hu originales

### Columnas de imágenes transformadas:
- `translated_*`: Momentos de la imagen trasladada
- `rotated_h1` a `rotated_h7`: Invariantes de Hu de imagen rotada 225°
- `escalated_h1` a `escalated_h7`: Invariantes de Hu de imagen escalada 1.5x

##  Uso

### Requisitos
```bash
pip install numpy pandas pillow matplotlib
```

### Ejecución
```bash
python main.py
```

El script procesará todas las imágenes en la carpeta `samples/` y generará:
- `Resultados_2D.csv`: Tabla con todas las características extractadas
- Imágenes binarizadas en la carpeta `binarized/`

##  Conceptos Clave

### Momentos de Imagen
Los momentos son descriptores estadísticos que capturan información sobre la forma y distribución de intensidad de píxeles.

### Invariantes de Hu
Son 7 funciones de momentos centrales normalizados que permanecen invariantes ante:
- **Translación**: Mediante el uso de momentos centrales
- **Escalado**: Mediante la normalización
- **Rotación**: Construcción matemática específica

### Componentes Conectados
- **4-conectado**: Píxeles vecinos en horizontal y vertical
- **8-conectado**: Incluye también diagonales

##  Validación de Invariancia

El proyecto verifica que los invariantes de Hu sean efectivamente invariantes comparando:
- Invariantes de la imagen original vs. rotada
- Invariantes de la imagen original vs. escalada

Esto valida la robustez de los descriptores ante transformaciones geométricas.

##  Referencias

- Hu, M. K. (1962). "Visual Pattern Recognition by Moment Invariants"
- Flusser, J., Suk, T., Zitová, B. (2016). "2D and 3D Image Analysis by Moments"

- Ralph, R. (s. f.). MPEG-7 Shape Database. DABI Lab - Temple University. https://dabi.temple.edu/external/shape/MPEG7/dataset.html

##  Notas

- El umbral de binarización está configurado en 128 (ajustable en `tools.py`)
- La rotación se aplica a 225° para evaluar invariancia
- El escalado se aplica con factor 1.5x
- La traslación se aplica con offset (100, 10) píxeles
## Licencia

Este proyecto está licenciado bajo la **MIT License** - ver el archivo [LICENSE](LICENSE) para más detalles.
---

**Autor**: Enrique Gómez  
**Institución**: Universidad Autónoma de Aguascalientes  
**Programa**: MCCMA - Nuevos Paradigmas Tecnológicos  
**Semestre**: Segundo Semestre
