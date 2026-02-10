import numpy as np

def connected_components(matrix:np.ndarray, neighbor:int = 4) -> int:
    rows, cols = matrix.shape
    visited_position = np.zeros((rows,cols), dtype=bool)

    if neighbor == 4:
        movements:list[tuple] = [(0,1), (0,-1), (-1,0), (1, 0)] 
    elif neighbor == 8:
        movements:list[tuple] = [(0,1), (0,-1), (-1,0), (1, 0), 
                                   (-1, 1), (-1, -1), (1, 1), (1, -1)] 
    else:
        return TypeError("Vecindad no permitida")
    
    num_objects:int = 0
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if matrix[i][j] == 1 and not visited_position[i][j]:
                num_objects += 1

                pile = [(i, j)]
                visited_position[i][j] = True

                while pile:
                    actual_row, actual_col = pile.pop()

                    for dr, dc in movements:
                        nr, nc = actual_row + dr, actual_col + dc
                        if matrix[nr][nc] == 1 and not visited_position[nr][nc]:
                            visited_position[nr][nc] = True
                            pile.append((nr, nc))

    return num_objects

def find_outline(matrix:np.ndarray, input_path:str, output_folder:str="outlines") -> dict:
    rows, cols = matrix.shape
    cont_outline = 0
    outline = np.zeros((rows, cols), dtype=int)
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if matrix[i][j] == 0:
                continue

            neighborhood_sum = (matrix[i, j-1] + matrix[i, j+1] + 
                                   matrix[i-1, j] + matrix[i+1, j])
            if neighborhood_sum < 4:
                outline[i][j] = 1
                cont_outline += 1
            else:
                outline[i][j] = 0

    #save_array_to_csv(outline, output_folder, input_path)
    return {"contorno": outline, "perimetro":cont_outline}