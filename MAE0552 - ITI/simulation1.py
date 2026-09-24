import numpy as np 


# FUNÇÕES DE ENTROPIA E INFORMAÇÃO MÚTUA

def entropy(x):
    # Convertendo a entrada para um array numpy 
    x = np.array(x,dtype=float)
    
    # Normalizando os valores para que a soma seja igual a 1 (Medida de Probabilidade)
    if not np.isclose(x.sum(),1):
        x = x/x.sum()
    
    # Pegando apenas medidas de probabilidade maiores que zero para evitar log(0)
    x = x[x>0]
    
    # Fórmula da entropia de Shannon: H(X) = -Σ p(x) log2(p(x))
    return -np.sum(x * np.log2(x))

def joint_entropy(x, y):
    
    # Convertendo as entradas para arrays numpy
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    
    # Normalizando os valores para que a soma seja igual a 1 (Medida de Probabilidade)
    if not np.isclose(x.sum(), 1):
        x = x / x.sum()
    if not np.isclose(y.sum(), 1):
        y = y / y.sum()
    
    # Calculando a entropia conjunta
    joint_prob = np.outer(x, y)
    joint_prob = joint_prob[joint_prob > 0]  # Evitando log(0)
    
    # Fórmula da entropia conjunta: H(X,Y) = -Σ p(x,y) log2(p(x,y))
    return -np.sum(joint_prob * np.log2(joint_prob))

def conditional_entropy(x, y):
    # Convertendo as entradas para arrays numpy
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    
    # Normalizando os valores para que a soma seja igual a 1 (Medida de Probabilidade)
    if not np.isclose(x.sum(), 1):
        x = x / x.sum()
    if not np.isclose(y.sum(), 1):
        y = y / y.sum()
    
    # Calculando a entropia condicional H(X|Y) = H(X,Y) - H(Y)
    h_xy = joint_entropy(x, y)
    h_y = entropy(y)
    
    return h_xy - h_y

def relative_entropy(x, y):
    
    kl_divergence = joint_entropy(x, y) - entropy(x)
    
    # Formula da divergência de Kullback-Leibler: D_KL(P||Q) = Σ p(x) log2(p(x)/q(x))
    # Fórmula alternativa: D_KL(P||Q) = H(P,Q) - H(P)
    
    return kl_divergence

def mutual_information(x, y):

    # Calculando a informação mútua I(X;Y) = H(X) + H(Y) - H(X,Y)
    h_x = entropy(x)
    h_y = entropy(y)
    h_xy = joint_entropy(x, y)
    
    return h_x + h_y - h_xy

def conditional_mutual_information(x, y, z):
    
    # Calculando a informação mútua condicional I(X;Y|Z) = H(X,Z) + H(Y,Z) - H(Z) - H(X,Y,Z)
    h_xz = joint_entropy(x, z)
    h_yz = joint_entropy(y, z)
    h_z = entropy(z)
    h_xyz = joint_entropy(np.outer(x, y), z)
    
    return h_xz + h_yz - h_z - h_xyz


# DEFINIÇÃO DO MODELO DE SIMULAÇÃO

# Probabilidade de Infecção na População (D = 1)
p_D1 = 0.3

# Taxa de Falso Positivo (T = 1 | D = 0)
p_fp = 0.1

# Taxa de Falso Negativo (T = 0 | D = 1)
p_fn = 0.25

# Desse modo criamos a seguinte tabela de probabilidades:
# D | T | Probabilidade 
# 0   0   P(D=0,T=0) = P(D=0) * P(T=0|D=0) = 0.7 * 0.9 = 0.63
# 0   1   P(D=0,T=1) = P(D=0) * P(T=1|D=0) = 0.7 * 0.1 = 0.07
# 1   0   P(D=1,T=0) = P(D=1) * P(T=0|D=1) = 0.3 * 0.25 = 0.075
# 1   1   P(D=1,T=1) = P(D=1) * P(T=1|D=1) = 0.3 * 0.75 = 0.225


# E as distribuições marginais de D e T são:
# P(D=0) = 0.7 || P(D=1) = 0.3
# P(T=0) = P(T=0,D=0) + P(T=0,D=1) = 0.63 + 0.075 = 0.705 || P(T=1) = P(T=1,D=0) + P(T=1,D=1) = 0.07 + 0.225 = 0.295

# Criando as distribuições de probabilidade para D e T

p_D = np.array([0.7, 0.3])       
p_T = np.array([0.705, 0.295])  

# Cálculo dos Valores Teóricos 

entropy_D = entropy(p_D)
print(f"Entropia de D: {entropy_D:.4f} bits")
entropy_T = entropy(p_T)
print(f"Entropia de T: {entropy_T:.4f} bits")

joint_entropy_DT = joint_entropy(p_D, p_T)
print(f"Entropia Conjunta de D e T: {joint_entropy_DT:.4f} bits")   

conditional_entropy_D_dado_T = conditional_entropy(p_D, p_T)    
print(f"Entropia Condicional de D dado T: {conditional_entropy_D_dado_T:.4f} bits")

conditional_entropy_T_dado_D = conditional_entropy(p_T, p_D)
print(f"Entropia Condicional de T dado D: {conditional_entropy_T_dado_D:.4f} bits")