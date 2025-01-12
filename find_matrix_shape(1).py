def find_mat_shape(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    return (rows, cols)
find_mat_shape([[9,8,0], [12,12,9], [8,0,7]])    
print(find_mat_shape([[9,8,0], [12,12,9], [8,0,7]])) 