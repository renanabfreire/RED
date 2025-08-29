import numpy as np
from scipy.linalg import lu_factor, lu_solve
from scipy.optimize import nnls

# Subsystems x Sources
subsystems = ["Shield", "Defence", "Fighter", "IonCannon", "Engines"]
sources = ["FusionCells", "HyperCores", "SolarCaps", "Geothermal", "Batteries"] # podem substituir alguma dessas últimas pelos ratos

#Vamos resolver com 3 métodos diferentes e comparar os resultados
#LU (scipy), Eliminação de Gauss  e Gauss-Seidel 

subsystems = ["Shield", "Defence", "Fighter", "IonCannon", "Engines"]
sources = ["FusionCells", "HyperCores", "SolarCaps", "Geothermal", "Batteries"]


#Achei que fazia mais sentido colocar quantos % de cada fonte eles vão pegar, ao invés de quantidade, mas podem mudar isso, não vai alterar o funcionamento
E = np.array([
    [0.4, 0.7, 0.6, 0.5, 0.0],   # Shield
    [0.3, 0.8, 0.2, 0.4, 0.5],   # Defence
    [0.5, 0.9, 0.3, 0.6, 0.4],   # Fighter
    [0.6, 0.7, 0.2, 0.5, 0.3],   # IonCannon
    [0.4, 0.6, 0.7, 0.8, 0.5],   # Engines
], dtype=float)

#Quantos de cada subsistemas existem
d = np.array([50, 120, 200, 100, 90], dtype=float)

#LU
#Caderno 8

# Consideraremos que as matrizes triangulares inferiores sempre terão a sua diagonal principal formada por entradas iguais a 1.
# L (triangular inferior) e U (triangular superior)
# piv: o vetor de pivoteamento
lu, piv = lu_factor(E) # Fatoração LU
x_lu = lu_solve((lu, piv), d) #Ex = d
res_lu = np.linalg.norm(E @ x_lu - d) # Calcula o resíduo do sistema: r = Ex−d
