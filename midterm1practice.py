import math
def secant_method(f, x0: int, x1: int, iterations: int) -> float:
    """Return the root calculated using the secant method."""
    xs = [x0, x1] + iterations * [None]  # Allocate x's vector

    for i, x in enumerate(xs):
        if i < iterations:
            x1 = xs[i+1]
            if f(x1) - f(x) == 0 : # to avoid division by 0 and return the last approximation
                return round(xs[i], 5)
            xs[i+2] = x1 - f(x1) * (x1 - x) / (f(x1) - f(x)) # fill component xs[i+2]
    
    return round(xs[-1], 5)  # Return the now filled last entry


def f(x):
    return math.pow(2.020, (-(math.pow(x, 3.0)))) - math.pow(x, 3.0)*math.cos(math.pow(x, 4.0)) - 1.984

root = secant_method(f, 1.5, 1.7, 100)

print("Root: {}".format(root))  # Root: 24.738633748750722


def naive_matrix_multiply(a, b):
    if(len(a[0]) != len(b)):
        raise Exception("Incompatible Matrixes for multiplication")
    rowmax = max(len(a), len(b))
    colmax = max(len(a[0]), len(b[0]))
    result = [[0 for x in range(colmax)] for y in range(rowmax)]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result
def matrix_add(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise Exception("Matrices have different size cannot add")
    result = [[0 for x in range(len(a[0]))] for y in range(len(a))]
    for i in range(len(a)): 
        for j in range(len(a[0])): 
            result[i][j] = a[i][j] + b[i][j]
    return result

def matrix_subtract(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise Exception("Matrices have different size cannot subtract")
    result = [[0 for x in range(len(a[0]))] for y in range(len(a))]
    for i in range(len(a)): 
        for j in range(len(a[0])): 
            result[i][j] = a[i][j] - b[i][j]
    return result

def strassen_matrix_split(a):
    "Assumes a square matrix"
    if math.ceil(math.log(len(a), 2)) != math.log(len(a), 2) or math.ceil(math.log(len(a[0]), 2)) != math.log(len(a[0]), 2):
        raise Exception('Non-power of 2 matrices are not supported!')
    matrix_length = len(a)
    mid = matrix_length // 2
    top_left = [[a[i][j] for j in range(mid)] for i in range(mid)]
    bot_left = [[a[i][j] for j in range(mid)] for i in range(mid, matrix_length)]
    top_right = [[a[i][j] for j in range(mid, matrix_length)] for i in range(mid)]
    bot_right = [[a[i][j] for j in range(mid, matrix_length)] for i in range(mid, matrix_length)]
    
    return top_left, top_right, bot_left, bot_right

def matrix_padding(a, newRow, newCol):
    newa = [[0 for x in range(newCol)] for y in range(newRow)]
    for i in range(len(a)):
        for j in range(len(a[i])):
            newa[i][j] = a[i][j]
    return newa


def strassen_matrix_multiply_helper(a, b):
    if(len(a[0]) != len(b)):
        raise Exception("Incompatible Matrixes for multiplication")
    rowmax = max(len(a), len(b))
    colmax = max(len(a[0]), len(b[0]))

    maxn = int(math.pow(2,math.ceil(math.log(max(rowmax, colmax), 2))))
    newa = matrix_padding(a, maxn, maxn)
    newb = matrix_padding(b, maxn, maxn)
    result = strassen_matrix_multiply(newa, newb)
    result = result[:rowmax]
    #prunes the padded rows and cols
    for i in range(len(result)):
        result[i] = result[i][:colmax]
    return result
def strassen_matrix_multiply(a, b):
    if len(a) == 2 and len(b) == 2:
        return naive_matrix_multiply(a, b)
    a11, a12, a21, a22 = strassen_matrix_split(a)
    b11, b12, b21, b22 = strassen_matrix_split(b)

    m1 = strassen_matrix_multiply(matrix_add(a11, a22), matrix_add(b11, b22))
    m2 = strassen_matrix_multiply(matrix_add(a21, a22), b11)
    m3 = strassen_matrix_multiply(a11, matrix_subtract(b12, b22))
    m4 = strassen_matrix_multiply(a22, matrix_subtract(b21, b11))
    m5 = strassen_matrix_multiply(matrix_add(a11, a12), b22)
    m6 = strassen_matrix_multiply(matrix_subtract(a21, a11), matrix_add(b11,b12))
    m7 = strassen_matrix_multiply(matrix_subtract(a12, a22), matrix_add(b21, b22))
    # Order of operations matter
    c11 = matrix_add(matrix_subtract(matrix_add(m1, m4), m5), m7)
    c12 = matrix_add(m3, m5)
    c21 = matrix_add(m2, m4)
    c22 = matrix_add(matrix_subtract(m1, m2), matrix_add(m3, m6))

    result = []
    for i in range(len(c11)):
        result.append(c11[i] + c12[i])
    for j in range(len(c21)):
        result.append(c21[j] + c22[j])
    return result
a = [[12, 7, 3], 
    [4, 5, 6], 
    [7, 8, 9]]

b = [[5, 8, 1, 2], 
    [6, 7, 3, 0], 
    [4, 5, 9, 1]] 

c = [[12, 7, 3, 0], 
    [4, 5, 6, 0], 
    [7, 8, 9, 0],
    [0, 0, 0, 0]]

d = [[5, 8, 1, 2], 
    [6, 7, 3, 0], 
    [4, 5, 9, 1],
    [0, 0, 0, 0]] 
for r in naive_matrix_multiply(a,b): 
    print(r)
print()
for r in strassen_matrix_multiply_helper(a,b): 
    print(r)
#Gaussian Elimination

def swap_row(m, i, j):
    temp = m[i]
    m[i] = m[j]
    m[j] = temp
    return m
def gauss_elimination(m):
    for i in range(len(m)):
        max_element = abs(m[i][i])
        max_row = i
        for j in range(i+1, len(m)):
            if abs(m[j][i]) > max_element:
                max_element = abs(m[j][i])
                max_row = j
        swap_row(m, i, max_row)
        #Forward elemination
        for j in range(i+1, len(m)):
            factor = m[j][i]/m[i][i]
            for k in range(i, len(m)+1):
                if i == k:
                    m[j][k] = 0
                else:
                    m[j][k] -= factor*m[i][k]
    # At this point, we have an upper triangular matrix
    # Back substitution
    x = [0]*len(m)
    for i in reversed(range(len(m))):
        x[i] = m[i][len(m)]/m[i][i]
        for j in reversed(range(len(m))):
            m[j][len(m)] -= m[j][i]*x[i]
    return x
m = [[.02, .01, 0, 0, .02],
     [  1,   2, 1, 0,   1],
     [  0,   1, 2, 1,   4],
     [0,0, 100, 200, 800]]
print(gauss_elimination(m))

# Power iteration as taken from wikipedia page
import numpy as np

def power_iteration(A, num_simulations: int):
    # Ideally choose a random vector
    # To decrease the chance that our vector
    # Is orthogonal to the eigenvector
    b_k = np.random.rand(A.shape[1])

    for _ in range(num_simulations):
        # calculate the matrix-by-vector product Ab
        b_k1 = np.dot(A, b_k)

        # calculate the norm
        b_k1_norm = np.linalg.norm(b_k1)

        # re normalize the vector
        b_k = b_k1 / b_k1_norm

    return b_k

print(power_iteration(np.array([[0.5, 0.5], [0.2, 0.8]]), 10))