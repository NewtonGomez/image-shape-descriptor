import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from image_moments import calc_central_moments, calc_hu_invariants
from image_transformations import rotate_image, translate_image
from tools import connected_components, find_outline

if __name__ == "__main__":
    csv_columns = ["Imagen", "Area", "# N4", "# N8", "# Contorno", 
                   "Original Centroid", "Central Momentums", "Original Hu",
                   "Traslated Centroid", "Traslated Momentums","Rotated Hu"]
    
    with open("Resultados_2D.csv", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=csv_columns)
        writer.writeheader()

        samples = np.array(os.listdir("samples"))

        for sample in samples:
            
            print("-----------------------------\n")
            break