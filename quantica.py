print ("Calculo em fisica: orbitais atomicos")

import numpy as np
import matplotlib.pyplot as plt

def lpmv(m, l, x):  # polinomios de legendre associados
    s = np.sqrt(np.clip(1 - x**2, 0, None))
    tabela = {
        (0, 1): x,
        (0, 2): (3 * x**2 - 1) / 2,
        (0, 3): (5 * x**3 - 3 * x) / 2,
        (1, 3): 1.5 * (5 * x**2 - 1) * s,
        (1, 4): 2.5 * (7 * x**3 - 3 * x) * s,
        (2, 4): 7.5 * (7 * x*2 - 1) * s*2,
    }
    return tabela[(m, l)]

# -- passo 1: visual (mesma paleta de cores escolhidas)

FUNDO = "#262626"
CORES = ["#ED7864", "#6E544F", "#7C909C", "#592F2F"]

# -- passo 2: orbitais (l, m) que serao desenhados ---
# l = tipo de orbital (1=p, 2=d, 3=f...), m = orientacao

ORBITAIS = [(1,0), (2,0), (3,0), (3,1), (4,1), (4,2)]
   # -- passo 3: angulos ---

theta = np.linspace(0, 2 * np.pi, 2000)

fig = plt.figure(figsize=(7, 7), facecolor=FUNDO)
ax = fig.add_subplot(projection="polar") 
ax.set_facecolor(FUNDO)
ax.axis("off")

     # ---passo 4: desenhar cada orbital como camada ---
      
for i, (l, m) in enumerate(ORBITAIS):
     
       # ---parte angular do orbital: | P_lˆm(cos 0) |
                   
  r =np.abs(lpmv(m, l, np.cos(theta)))
                   
     # --- normaliza e auemnta o tamanho de cada camada (como as camadas n)
r = r / r.max() * (1 + i * 0.45)
        
        # --- passo5: simetria de flor (4 giros de 45 graus) ---
        
for k in range(4):
     ax.plot(theta + k * np.pi / 4, r, color=CORES[i % len(CORES)], lw=1.2)
             
plt.show()