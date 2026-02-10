import numpy as np

def scalate_image(imagen, scale):
    rows, cols = imagen.shape
    
    nuevo_alto = int(rows * scale)
    nuevo_ancho = int(cols * scale)
    
    row_indices = (np.arange(nuevo_alto) / scale).astype(int)
    col_indices = (np.arange(nuevo_ancho) / scale).astype(int)
    row_indices = np.clip(row_indices, 0, rows - 1)
    col_indices = np.clip(col_indices, 0, cols - 1)
    imagen_nueva = imagen[np.ix_(row_indices, col_indices)]
    
    return imagen_nueva

def rotate_image(matrix:np.ndarray, centroid:tuple, angle:int = 45) -> np.ndarray:
    rows, cols = matrix.shape
    rotated_img = np.zeros_like(matrix)
    cx, cy = centroid

    centroid_x_destiny = cx
    centroid_y_destiny = cy

    theta = np.radians(angle)
    cos_t = np.cos(theta)
    sin_t = np.sin(theta)

    grid_y, grid_x = np.indices((rows, cols))

    x_relation = grid_x - centroid_x_destiny
    y_relation = grid_y - centroid_y_destiny

    src_x_rel = (x_relation * cos_t) + (y_relation* sin_t)
    src_y_rel = -(x_relation * sin_t) + (y_relation * cos_t)

    src_x = src_x_rel + cx
    src_y = src_y_rel + cy
    
    src_x_int = np.round(src_x).astype(int)
    src_y_int = np.round(src_y).astype(int)
    
    valid_mask = (
        (src_x_int >= 0) & 
        (src_x_int < cols) & 
        (src_y_int >= 0) & 
        (src_y_int < rows)
    )

    rotated_img[valid_mask] = matrix[
        src_y_int[valid_mask],
        src_x_int[valid_mask]
    ]

    return rotated_img

def translate_image(matrix: np.ndarray, x1: int, y1: int) -> np.ndarray:
    translated = np.zeros_like(matrix)
    
    rows, cols = matrix.shape[:2]
    
    if x1 > 0:
        src_x_start, src_x_end = 0, cols - x1
        dst_x_start, dst_x_end = x1, cols
    else:
        src_x_start, src_x_end = -x1, cols
        dst_x_start, dst_x_end = 0, cols + x1
        
    if y1 > 0:
        src_y_start, src_y_end = 0, rows - y1
        dst_y_start, dst_y_end = y1, rows
    else:
        src_y_start, src_y_end = -y1, rows
        dst_y_start, dst_y_end = 0, rows + y1

    if src_x_start < src_x_end and src_y_start < src_y_end:
        translated[dst_y_start:dst_y_end, dst_x_start:dst_x_end] = \
            matrix[src_y_start:src_y_end, src_x_start:src_x_end]
            
    return translated