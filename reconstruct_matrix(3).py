import numpy as np

def reconstruct_matrix(U, S, V):
    
    return np.dot(U, np.dot(np.diag(S), V))
reconstruct_matrix([[1, 2], [3, 4]], [1, 0], [[1, 0], [0, 1]])
print(reconstruct_matrix([[1, 2], [3, 4]], [1, 0], [[1, 0], [0, 1]]))