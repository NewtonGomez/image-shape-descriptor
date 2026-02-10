import numpy as np

def calc_central_moments(matrix:np.ndarray) -> dict:
    rows, cols = matrix.shape
    y_coords, x_coords = np.mgrid[:rows, :cols]
    
    x_diff = x_coords - cx
    y_diff = y_coords - cy

    def get_mu(p, q):
        termino = (x_diff ** p) * (y_diff ** q) * matrix
        return np.sum(termino)
    
    mu_00 = get_mu(0, 0)

    mu_10 = np.sum(x_coords * matrix)
    mu_01 = np.sum(y_coords * matrix)

    cx = mu_10 / mu_00
    cy = mu_01 / mu_00

    def get_eta(p, q):
        mu_val = get_mu(p, q)
        gamma = (p + q) / 2 + 1
        return float(mu_val / (mu_00 ** gamma))

    return {
        "eta_00":get_eta(0, 0),
        "eta_01":get_eta(0, 1),
        "eta_10":get_eta(1, 0),
        "eta_11":get_eta(1, 1),
        "eta_02":get_eta(0, 2),
        "eta_20":get_eta(2, 0),
        "eta_21":get_eta(2, 1),
        "eta_12":get_eta(1, 2),
        "eta_03":get_eta(0, 3),
        "eta_30":get_eta(3, 0)
    }

def calc_hu_invariants(eta_dict:dict) -> dict:
    eta_20 = eta_dict["eta_20"]
    eta_02 = eta_dict["eta_02"]
    eta_11 = eta_dict["eta_11"]
    eta_30 = eta_dict["eta_30"]
    eta_12 = eta_dict["eta_12"]
    eta_21 = eta_dict["eta_21"]
    eta_03 = eta_dict["eta_03"]

    h1 = eta_20 + eta_02
    
    h2 = (eta_20 - eta_02)**2 + 4 * eta_11**2
    
    h3 = (eta_30 - 3 * eta_12)**2 + (3 * eta_21 - eta_03)**2
    
    h4 = (eta_30 + eta_12)**2 + (eta_21 + eta_03)**2
    
    h5 = (eta_30 - 3 * eta_12) * (eta_30 + eta_12) * \
         ((eta_30 + eta_12)**2 - 3 * (eta_21 + eta_03)**2) + \
         (3 * eta_21 - eta_03) * (eta_21 + eta_03) * \
         (3 * (eta_30 + eta_12)**2 - (eta_21 + eta_03)**2)
         
    h6 = (eta_20 - eta_02) * ((eta_30 + eta_12)**2 - (eta_21 + eta_03)**2) + \
         4 * eta_11 * (eta_30 + eta_12) * (eta_21 + eta_03)
         
    h7 = (3 * eta_21 - eta_03) * (eta_30 + eta_12) * \
         ((eta_30 + eta_12)**2 - 3 * (eta_21 + eta_03)**2) - \
         (eta_30 - 3 * eta_12) * (eta_21 + eta_03) * \
         (3 * (eta_30 + eta_12)**2 - (eta_21 + eta_03)**2)

    # 3. Retorno del diccionario
    return {
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "h6": h6,
        "h7": h7
    }