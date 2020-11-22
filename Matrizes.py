import numpy as np



print("Matrizes da Simulação 1")
print("A:")
Sim_1_A = np.matrix('0.07, 0, 0; 0.93, 0.2, 0; 0, 0.8, 1') 
print(Sim_1_A)
print("U0:")
Sim_1_U0 = np.matrix('202206486; 5276942; 4721593 ')
print(Sim_1_U0)

print('#####################################################')

print("Matrizes da Simulação 2")
print("A:")
Sim_2_A = np.matrix('0.27, 0, 0; 0.73, 0.36, 0; 0, 0.64, 1') 
print(Sim_2_A)
print("U0:")
Sim_2_U0 = np.matrix('7744985128; 46643798; 31156914 ')
print(Sim_2_U0)

print('#####################################################')

print("Matrizes da Simulação 3")
print("A:")
Sim_3_A = np.matrix('0.8, 0, 0; 0.2, 0.36, 0; 0, 0.64, 1') 
print(Sim_3_A)
print("U0:")
Sim_3_U0 = np.matrix('7744985128; 46643798; 31156914 ')
print(Sim_3_U0)

print('#####################################################')

print("Matrizes da Simulação 4")
print("A:")
Sim_4_A = np.matrix('0.38, 0, 0; 0.62, 0.19, 0; 0, 0.81, 1') 
print(Sim_4_A)
print("U0:")
Sim_4_U0 = np.matrix('234; 1396; 0 ')
print(Sim_4_U0)

print('#####################################################')

print("Matrizes da Simulação 5")
print("A:")
Sim_5_A = np.matrix('0.25, 0, 0; 0.75, 0.8, 0; 0, 0.2, 1') 
print(Sim_5_A)
print("U0:")
Sim_5_U0 = np.matrix('59009; 166521; 0 ')
print(Sim_5_U0)

print('#####################################################')

print("Matrizes da Simulação 7")
print("A:")
Sim_7_A = np.matrix('0.27, 0, 0; 0.73, 0.36, 0; 0, 0.64, 1')
print(Sim_7_A)
print("U0:")
Sim_7_U0 = np.matrix('7822785839; 1; 0 ')
print(Sim_7_U0)

res = [[0 for x in range(3)] for y in range(3)]  

def mult(X,Y):
# explicit for loops 
    for i in range(len(X)): 
        for j in range(len(Y[0])): 
            for k in range(len(Y)): 
            # resulted matrix 
                res[i][j] += X[i][k] * Y[k][j] 
                print (res) 
            