import numpy as np
""" 
    Metode Euler (yi+1 = yi+f(ti,yi)*h)
    Fungsi (f(t,y) = -(exp(t)) / -(y ** 2))
    Diketahui h = 0.001, t = 100, dan iterasi sebanyak 100000
    Ditanyakan nilai y ketika t = 100
"""
h = 0.001
t = 100
iteration = int(t/h)
ti = np.zeros(iteration+1)
yi = np.zeros(iteration+1)
ti[0] = 0
yi[0] = 1

def f(t,y):
    return (-(np.exp(t))) / (-(y**2))

for i in range(iteration):
    t = ti[i]
    y = yi[i]
    yiplus1 = y+f(t,y)*h
    
    ti[i+1] = t+h
    yi[i+1] = yiplus1
    
print(f"Jadi nilai y ketika t = 100 adalah {yi[-1]}")


