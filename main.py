import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from image_moments import calc_central_moments, calc_hu_invariants
from image_transformations import rotate_image, translate_image, scalate_image
from tools import connected_components, find_outline, process_and_binarize, save_matrix_to_csv

if __name__ == "__main__":
    csv_columns = ['Imagen', 'Area', 'N4', 'N8', 'Contorno_Perimetro', 'm00', 'centroid', 
                   'eta_00', 'eta_10', 'eta_01', 'eta_11', 'eta_02', 'eta_20', 'eta_21', 
                   'eta_12', 'eta_03', 'eta_30', 'mass_h1', 'mass_h2', 'mass_h3', 'mass_h4', 
                   'mass_h5', 'mass_h6', 'mass_h7', 'translated_m00', 'translated_centroid', 
                   'translated_eta_00', 'translated_eta_10', 'translated_eta_01', 'translated_eta_11', 
                   'translated_eta_02', 'translated_eta_20', 'translated_eta_21', 'translated_eta_12', 
                   'translated_eta_03', 'translated_eta_30', 'rotated_mass_h1_225', 'rotated_mass_h2_225', 
                   'rotated_mass_h3_225', 'rotated_mass_h4_225', 'rotated_mass_h5_225', 'rotated_mass_h6_225', 
                   'rotated_mass_h7_225', 'rotated_mass_h1_180', 'rotated_mass_h2_180', 'rotated_mass_h3_180', 
                   'rotated_mass_h4_180', 'rotated_mass_h5_180', 'rotated_mass_h6_180', 'rotated_mass_h7_180', 
                   'rotated_mass_h1_45', 'rotated_mass_h2_45', 'rotated_mass_h3_45', 'rotated_mass_h4_45', 
                   'rotated_mass_h5_45', 'rotated_mass_h6_45', 'rotated_mass_h7_45', 'h1', 'h2', 'h3', 'h4', 
                   'h5', 'h6', 'h7', 'rotated_outline_h1_225', 'rotated_outline_h2_225', 'rotated_outline_h3_225', 
                   'rotated_outline_h4_225', 'rotated_outline_h5_225', 'rotated_outline_h6_225', 'rotated_outline_h7_225', 
                   'rotated_outline_h1_180', 'rotated_outline_h2_180', 'rotated_outline_h3_180', 'rotated_outline_h4_180', 
                   'rotated_outline_h5_180', 'rotated_outline_h6_180', 'rotated_outline_h7_180', 'rotated_outline_h1_45', 
                   'rotated_outline_h2_45', 'rotated_outline_h3_45', 'rotated_outline_h4_45', 'rotated_outline_h5_45', 
                   'rotated_outline_h6_45', 'rotated_outline_h7_45', 'escalated_h1', 'escalated_h2', 'escalated_h3', 
                   'escalated_h4', 'escalated_h5', 'escalated_h6', 'escalated_h7']
    
    with open("Resultados_2D.csv", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=csv_columns)
        writer.writeheader()

        samples = np.array(os.listdir("samples"))

        for sample in samples:
            bin_image = process_and_binarize(sample)
            outline = find_outline(bin_image)
            central_moments = calc_central_moments(bin_image)
            cen_hu_mass = calc_hu_invariants(central_moments)
            cen_mom_outline = calc_central_moments(outline["contorno"])
            cen_hu_outline = calc_hu_invariants(cen_mom_outline)
            

            quantty_n4 = connected_components(bin_image)
            quantty_n8 = connected_components(bin_image, neighbor=8)

            translated_image = translate_image(bin_image, 100, 10)
            trans_cen_mom = calc_central_moments(translated_image)

            rot_image = rotate_image(bin_image, central_moments["centroid"], 225)
            rot_cen_mom = calc_central_moments(rot_image)
            rot_hu_225 = calc_hu_invariants(rot_cen_mom)
            rot_225_outline = find_outline(rot_image)
            rot_cen_mom_225_outline = calc_central_moments(rot_225_outline["contorno"])
            rot_hu_225_outline = calc_hu_invariants(rot_cen_mom_225_outline)

            
            rot_image_180 = rotate_image(bin_image, central_moments["centroid"], 180)
            rot_cen_mom_180 = calc_central_moments(rot_image_180)
            rot_hu_180 = calc_hu_invariants(rot_cen_mom_180)
            rot_180_outline = find_outline(rot_image_180)
            rot_cen_mom_180_outline = calc_central_moments(rot_180_outline["contorno"])
            rot_hu_180_outline = calc_hu_invariants(rot_cen_mom_180_outline)
            
            rot_image_45 = rotate_image(bin_image, central_moments["centroid"], 45)
            rot_cen_mom_45= calc_central_moments(rot_image_45)
            rot_hu_45 = calc_hu_invariants(rot_cen_mom_45) 
            rot_45_outline = find_outline(rot_image_45)
            rot_cen_mom_45_outline = calc_central_moments(rot_45_outline["contorno"])
            rot_hu_45_outline = calc_hu_invariants(rot_cen_mom_45_outline)

            escalated_img = scalate_image(bin_image, 1.5)
            esc_cen_mom = calc_central_moments(escalated_img)
            esc_hu = calc_hu_invariants(esc_cen_mom)
            
            row = {
                "Imagen": sample,
                "Area": central_moments["m00"],
                "N4": quantty_n4,
                "N8": quantty_n8,
                "Contorno_Perimetro": outline["perimetro"]
            }
            
            cen_hu_mass = {f"mass_{k}": v for k, v in cen_hu_mass.items()}
            trans_cen_mom = {f"translated_{k}": v for k, v in trans_cen_mom.items()}
            rot_hu_225 = {f"rotated_mass_{k}_225": v for k, v in rot_hu_225.items()}
            rot_hu_180 = {f"rotated_mass_{k}_180": v for k, v in rot_hu_180.items()}
            rot_hu_45 = {f"rotated_mass_{k}_45": v for k, v in rot_hu_45.items()}
            rot_hu_225_outline = {f"rotated_outline_{k}_225": v for k, v in rot_hu_225_outline.items()}
            rot_hu_180_outline = {f"rotated_outline_{k}_180": v for k, v in rot_hu_180_outline.items()}
            rot_hu_45_outline = {f"rotated_outline_{k}_45": v for k, v in rot_hu_45_outline.items()}
            compare_hu_escalated= {f"escalated_{k}": v for k, v in esc_hu.items()}

            row.update(central_moments)
            row.update(cen_hu_mass)
            row.update(trans_cen_mom)
            row.update(rot_hu_225)
            row.update(rot_hu_180)
            row.update(rot_hu_45)
            row.update(cen_hu_outline)
            row.update(rot_hu_225_outline)
            row.update(rot_hu_180_outline)
            row.update(rot_hu_45_outline)
            row.update(compare_hu_escalated)

            writer.writerow(row)

            # ---- save data
            save_matrix_to_csv(bin_image, f"data/originals/{sample}")
            save_matrix_to_csv(rot_image, f"data/rotated/225_{sample}")
            save_matrix_to_csv(rot_image_180, f"data/rotated/180_{sample}")
            save_matrix_to_csv(rot_image_45, f"data/rotated/45_{sample}")
            save_matrix_to_csv(translated_image, f"data/translated/{sample}")
            save_matrix_to_csv(escalated_img, f"data/scalated/{sample}")

            # ---- graficas

            max_alto = max(bin_image.shape[0], bin_image.shape[0])
            max_ancho = max(bin_image.shape[1], bin_image.shape[1])

            plt.figure(figsize=(12, 6))

            plt.subplot(2, 3, 1)
            plt.title("Imagen Original")
            plt.axis('off')
            plt.imshow(bin_image, cmap="gray")

            plt.subplot(2, 3, 2)
            plt.title("Imagen Trasladada")
            plt.axis('off')
            plt.imshow(translated_image, cmap="gray")

            plt.subplot(2, 3, 6)
            plt.axis('off')
            plt.title("Imagen Rotada 225º")
            plt.imshow(rot_image, cmap="gray")

            plt.subplot(2, 3, 5)
            plt.axis('off')
            plt.title("Imagen Rotada 180º")
            plt.imshow(rot_image_180, cmap="gray")
            plt.subplot(2, 3, 4)
            plt.axis('off')
            plt.title("Imagen Rotada 45º")
            plt.imshow(rot_image_45, cmap="gray")

            plt.subplot(2, 3, 3)
            plt.axis('off')
            plt.title("Imagen Escalada")
            plt.imshow(escalated_img, cmap="gray")
            plt.xlim(0, max_ancho)
            plt.ylim(max_alto, 0)
            plt.gca().set_aspect('equal', adjustable='box')

            plt.tight_layout()
            if not sample.endswith('.png') and not sample.endswith('.jpg'):
                filename = f"graphs/{sample.split(".")[0]}.png"
                
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print("-----------------------------\n")