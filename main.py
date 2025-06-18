import numpy as np
import time
import matplotlib.pyplot as plt

def gauss_elimination(A, b):
    n = len(b)
    for i in range(n):
        max_row = i
        for j in range(i+1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            A[j][i:] -= factor * A[i][i:]
            b[j] -= factor * b[i]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i][i+1:], x[i+1:])) / A[i][i]
    return x

def lu_factorization(A, b):
    n = len(b)
    L = np.eye(n)
    U = A.copy()
    for i in range(n):
        for j in range(i+1, n):
            factor = U[j][i] / U[i][i]
            L[j][i] = factor
            U[j][i:] -= factor * U[i][i:]
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i][:i], y[:i])
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i][i+1:], x[i+1:])) / U[i][i]
    return x

def measure_time(algorithm, A, b):
    start_time = time.time()
    algorithm(A, b)
    return time.time() - start_time

sizes = [100, 400, 500, 700, 1000, 1500, 2000]
gauss_times = []
lu_times = []

for n in sizes:
    A = np.random.rand(n, n)
    b = np.random.rand(n)
    
    gauss_time = measure_time(gauss_elimination, A.copy(), b.copy())
    lu_time = measure_time(lu_factorization, A.copy(), b.copy())
    
    gauss_times.append(gauss_time)
    lu_times.append(lu_time)

plt.plot(sizes, gauss_times, label='Gauss Elimination')
plt.plot(sizes, lu_times, label='LU Factorization')
plt.xlabel('Matrix Size')
plt.ylabel('Execution Time (s)')
plt.title('Performance Comparison: Gauss vs LU')
plt.legend()
plt.show()


print("Temps d'exécution pour Gauss Elimination:", gauss_times)
print("Temps d'exécution pour LU Factorization:", lu_times)