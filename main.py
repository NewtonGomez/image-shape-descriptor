import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from image_moments import calc_central_moments, calc_hu_invariants
from image_transformations import rotate_image, translate_image
from tools import connected_components, find_outline, process_and_binarize

if __name__ == "__main__":
    csv_columns = ['Imagen', 'Area', 'N4', 'N8', 'Contorno_Perimetro', 'm00', 'centroid', 
                   'eta_00', 'eta_10', 'eta_01', 'eta_11', 'eta_02', 'eta_20', 'eta_21', 'eta_12', 'eta_03', 'eta_30', 
                   'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 
                   'translated_m00', 'translated_centroid', 'translated_eta_00', 'translated_eta_10', 
                   'translated_eta_01', 'translated_eta_11', 'translated_eta_02', 'translated_eta_20', 
                   'translated_eta_21', 'translated_eta_12', 'translated_eta_03', 'translated_eta_30', 
                   'rotated_h1', 'rotated_h2', 'rotated_h3', 'rotated_h4', 'rotated_h5', 'rotated_h6', 'rotated_h7']
    
    with open("Resultados_2D.csv", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=csv_columns)
        writer.writeheader()

        samples = np.array(os.listdir("samples"))

        for sample in samples:
            bin_image = process_and_binarize(sample)
            central_moments = calc_central_moments(bin_image)
            cen_hu = calc_hu_invariants(central_moments)

            quantty_n4 = connected_components(bin_image)
            quantty_n8 = connected_components(bin_image, neighbor=8)
            outline = find_outline(bin_image)

            translated_image = translate_image(bin_image, 100, 10)
            trans_cen_mom = calc_central_moments(translated_image)

            rot_image = rotate_image(bin_image, central_moments["centroid"], 225)
            rot_cen_mom = calc_central_moments(rot_image)
            rot_hu = calc_hu_invariants(rot_cen_mom)
            
            row = {
                "Imagen": sample,
                "Area": central_moments["m00"],
                "N4": quantty_n4,
                "N8": quantty_n8,
                "Contorno_Perimetro": outline["perimetro"]
            }

            # ---- impresion de informacin
            df_basic = pd.Series({k: row[k] for k in row.keys()})
            print("\nMétricas Básicas:")
            print(df_basic.to_string())

            compare_cen = pd.DataFrame({
                "Original": [central_moments[k] for k in central_moments.keys()],
                "Rotado": [trans_cen_mom[k] for k in trans_cen_mom.keys()]
            }, index=central_moments.keys())
            print("\n Comparación Momentos (Invarianza a Traslacion):")
            print(compare_cen.iloc[5:].map(lambda x: f"{x:.6f}"))
            
            compare_hu = pd.DataFrame({
                "Original": [cen_hu[k] for k in cen_hu.keys()],
                "Rotado": [rot_hu[k] for k in rot_hu.keys()]
            }, index=cen_hu.keys())
            print("\n Comparación Hu (Invarianza a Rotación):")
            print(compare_hu.map(lambda x: f"{x:.4f}"))

            trans_cen_mom = {f"translated_{k}": v for k, v in trans_cen_mom.items()}
            rot_hu = {f"rotated_{k}": v for k, v in rot_hu.items()}
            row.update(central_moments)
            row.update(cen_hu)
            row.update(trans_cen_mom)
            row.update(rot_hu)

            writer.writerow(row)

            # ---- graficas
            '''
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
            plt.axis('off')
            plt.title("Imagen Rotada")
            plt.imshow(rot_image, cmap="gray")
            plt.tight_layout()
            plt.show()
            '''
            print("-----------------------------\n")
            break