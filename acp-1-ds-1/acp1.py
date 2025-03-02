def multiply_one_iteration(N, M):
    return N * M 
 # Total iterations = 1 

print(multiply_one_iteration(5, 4))  

def multiply_n_iterations(N, M):
    result = 0
    for _ in range(M):  
        result += N  
    return result
