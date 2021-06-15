import numpy as np
import matplotlib as plt


def seq_a(n):
    y = [1]
    for k in range (1,n):
        y.append(y[-1]+ 2)
    return y

def seq_b(n):
    y = [1]
    for k in range (1,n):
        y.append(y[-1]+ k+1)
    return y

def seq_c(n):
    y = [1]
    for  k in range (1,n):
        y.append((k+1)**2)
    return y



n = 20  
print(seq_a(n))
print(seq_b(n))
print(seq_c(n))
