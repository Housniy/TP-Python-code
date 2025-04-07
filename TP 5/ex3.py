import numpy as np

tableau = np.arange(12)
print("Tableau 1D :", tableau)

tableau_2d = tableau.reshape(3, 4)
print("Tableau 2D (3x4) :\n", tableau_2d)

tableau_3d = tableau.reshape(2, 2, 3)
print("Tableau 3D (2x2x3) :\n", tableau_3d)

tableau_2d_transpose = tableau_2d.T
print("Tableau 2D transposé :\n", tableau_2d_transpose)

tableau_2d_axes_inverses = np.swapaxes(tableau_2d, 0, 1)
print("Tableau 2D après swapaxes :\n", tableau_2d_axes_inverses)

tableau1_2d = np.array([[1, 2, 3], [4, 5, 6]])
tableau2_2d = np.array([[7, 8, 9], [10, 11, 12]])

concat_verticale = np.vstack((tableau1_2d, tableau2_2d))
print("Concaténation verticale :\n", concat_verticale)

concat_horizontale = np.hstack((tableau1_2d, tableau2_2d))
print("Concaténation horizontale :\n", concat_horizontale)

sous_tableaux = np.hsplit(concat_horizontale, 2)
print("Sous-tableau 1 :\n", sous_tableaux[0])
print("Sous-tableau 2 :\n", sous_tableaux[1])
