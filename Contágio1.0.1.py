#Modelo de Contágio

N = 1 #número de indivíduos
t = 1 #número de dias
I0 = 1 #número de infectados inicial
S0 = 1 #número de suscetíveis inicial
m = 1 #probabilidade de tratamento
c = 1 #probabilidade de contágio
k = 1 #média de indivíduos próximos
R0 = k*c/m
 
I(t) = I0 + (c*(k*(I0/N))*(N-I0))-m*I0
S(t) = N - I(t)
