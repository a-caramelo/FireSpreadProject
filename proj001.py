import numpy as np
import imageio

#Cell States
# 0 - Clear/Terra
# 1 - Fuel
# 2 - Fire
# 3 - Arvore 1
# 4 - Arvore 2
# 5 - Arvore 3
# 6 - Agua

# Prob de ser fuel
prob1=0.1
# prob de ser arvore 1
prob_arv1 = 0.3
# prob de ser arvore 2
prob_arv2 = 0.2
# prob de ser arvore 3
prob_arv3 = 0.2

# Tamanho da imagem (grelha)
terrain_size = [30,30]
# Tempo de simulação/ nr de iterações
total_time = 1

# Vai guardar a simulacao toda basicamente, vai ter t grelhas
states = np.zeros((total_time, *terrain_size))


# Cria o estado inicial, cria matriz do tamanho da grelha c nr e probabilidades atribuidas 

states[0] = np.random.choice([0,1,2,3,4],size=terrain_size,p=[1-prob1-prob_arv1-prob_arv2-prob_arv3,prob1,prob_arv1,prob_arv2,prob_arv3]) 

print(states[0])

colored = np.zeros((total_time,*terrain_size,3),dtype=np.uint8)


t=0
for x in range(states[t].shape[0]):
        for y in range(states[t].shape[1]):
            value = states[t,x,y].copy()

            if value == 0:
                colored[t,x,y] = [139,69,19] # Clear
            elif value == 1:
                colored[t,x,y] = [0,0,0]   # Fuel
            elif value == 2:
                colored[t,x,y] = [0,255,0]   # Arvore 1

            elif value == 3:
                colored[t,x,y] = [0,77,13]   # Arvore 2

            elif value == 4:
                colored[t,x,y] = [0,179,13]   # Arvore 3



print(states.shape[0])


imageio.mimsave('./video.gif', colored)



