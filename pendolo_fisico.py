import numpy as np 
from matplotlib import pyplot as plt 
from scipy.optimize import curve_fit 
# Dati---mettete le vostre misure! 
# Qui potete anche leggere i dati da file, usando il metodo np.loadtxt(), 
# se lo trovate comodo. 
L = np.array([0.95, 0.85, 0.75, 0.65, 0.55, 0.45, 0.35, 0.25, 0.15, 0.05])
d = abs(L - 0.525)
sigma_d = np.full(d.shape, 0.002) 
T = np.array([15.9, 15.4, 15.7, 18.3, 38.1, 22.7, 16.7, 15.61, 15.7, 16.3])
T = T/10 
sigma_T = np.array([0.2, 0.1, 0.1, 0.2, 0.2, 0.1, 0.1, 0.06, 0.1, 0.1])
sigma_T = sigma_T/10 
# Definizione dell’accelerazione di gravita‘. 
g = 9.81 
def period_model(d, l): 
 """Modello per il periodo del pendolo. 
 """ 
 return 2.0 * np.pi * np.sqrt((l**2.0 / 12.0 + d**2.0) / (g * d)) 
plt.figure("Periodo")
# Scatter plot dei dati. 
plt.errorbar(d, T, sigma_T, sigma_d, fmt="o") 
# Fit---notate che questo e‘ un fit ad un solo parametro. 
popt, pcov = curve_fit(period_model, d, T, sigma=sigma_T) 
l_hat = popt[0] 
sigma_l = np.sqrt(pcov[0, 0]) 
# Confrontate i parametri di best fit con la vostra misura diretta! 
print(l_hat, sigma_l) 
# Grafico del modello di best-fit. 
x = np.linspace(0.01, 0.5, 100) 
plt.plot(x, period_model(x, l_hat)) 
plt.xlabel("d [m]") 
plt.ylabel("Periodo [s]")
plt.grid(which="both", ls="dashed", color="gray")
r = T - period_model(d, l=1.05)
sigma_r = sigma_T
plt.savefig("massa_raggio.pdf") 
plt.show()
plt.plot(d, r, linestyle='', marker='o')
plt.errorbar(d, r, sigma_r, sigma_d, fmt="o")
plt.show()