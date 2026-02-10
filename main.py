import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from image_moments import calc_central_moments, calc_hu_invariants
from image_transformations import rotate_image, translate_image
from tools import connected_components, find_outline, process_and_binarize

if __name__ == "__main__":
    csv_columns = ["Imagen", "Area", "# N4", "# N8", "# Contorno", 
                   "Original Centroid", "Central Momentums", "Original Hu",
                   "Traslated Centroid", "Traslated Momentums","Rotated Hu"]
    
    with open("Resultados_2D.csv", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=csv_columns)
        writer.writeheader()

        samples = np.array(os.listdir("samples"))

        for sample in samples:
            bin_image = process_and_binarize(sample)
            central_moments = calc_central_moments(bin_image)

            translated_image = translate_image(bin_image, 100, 10)
            trans_cen_mom = calc_central_moments(translated_image)

            rot_image = rotate_image(bin_image, central_moments["centroid"], 225)
            rot_cen_mom = calc_central_moments(rot_image)
            print(central_moments)
            print(trans_cen_mom)
            print(calc_hu_invariants(central_moments))
            print(calc_hu_invariants(rot_cen_mom))

            plt.figure(figsize=(12, 6))
            plt.subplot(1, 3, 1)
            plt.title("Imagen Original")
            plt.axis('off')
            plt.imshow(bin_image, cmap="gray")
            plt.subplot(1, 3, 2)
            plt.title("Imagen Trasladada")
            plt.axis('off')
            plt.imshow(translated_image, cmap="gray")
            plt.subplot(1, 3, 3)
            plt.title("Imagen Rotada")
            plt.imshow(rot_image, cmap="gray")
            plt.tight_layout()
            plt.axis('off')
            plt.show()

            print("-----------------------------\n")
            break