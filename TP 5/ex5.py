import numpy as np
import matplotlib.pyplot as plt

# 1. Matrice de covariance
# Créer un tableau de données aléatoires de dimensions (100, 3)
donnees = np.random.rand(100, 3)
# Calculer la matrice de covariance
matrice_covariance = np.cov(donnees, rowvar=False)
print("Matrice de covariance :\n", matrice_covariance)

# 2. Transformation de Fourier
# Créer un tableau de données sinusoïdales
temps = np.linspace(0, 1, 500)  # 500 points entre 0 et 1 seconde
frequence = 5  # Fréquence en Hz
signal = np.sin(2 * np.pi * frequence * temps)

# Appliquer la transformation de Fourier
spectre = np.fft.fft(signal)
frequences = np.fft.fftfreq(len(signal), d=(temps[1] - temps[0]))


# 3. Histogramme des sommes de lancers de dés
# Simuler 1000 lancers de deux dés
des1 = np.random.randint(1, 7, size=1000)  # Lancer du premier dé
des2 = np.random.randint(1, 7, size=1000)  # Lancer du deuxième dé
somme_des = des1 + des2

# Afficher l'histogramme des sommes
plt.figure(figsize=(8, 5))
plt.hist(somme_des, bins=11, range=(2, 12), color='skyblue', edgecolor='black', density=True)
plt.title("Histogramme des sommes de deux dés (1000 lancers)")
plt.xlabel("Somme obtenue")
plt.ylabel("Fréquence")
plt.grid(axis='y')
plt.show()
