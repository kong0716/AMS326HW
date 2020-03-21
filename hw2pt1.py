# Darren Kong
# 110770716
# AMS326

import math, numpy as np, time
naive_addition = 0
naive_multiply = 0
strassen_addition = 0
strassen_multiply = 0
def naive_matrix_multiply(a, b):
    #global naive_addition, naive_multiply
    if(len(a[0]) != len(b)):
        raise Exception("Incompatible Matrixes for multiplication")
    rowmax = max(len(a), len(b))
    colmax = max(len(a[0]), len(b[0]))
    result = [[0 for x in range(colmax)] for y in range(rowmax)]
    for i in range(len(a)):
        print(i)
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
                #naive_addition += 1
                #naive_multiply += 1
    #result += [[[a[i][k] * b[k][j] for k in range(len(b))] for j in range(len(b[0]))] for i in range(len(a))]
    #naive_addition += len(a)**3
    #naive_multiply += len(a)**3
    return result
def matrix_add(a, b):
    #global strassen_addition
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise Exception("Matrices have different size cannot add")
    result = [[a[i][j] + b[i][j]  for j in range(len(a[0]))] for i in range(len(a))]
    #strassen_addition += len(a)**2
    return result
def matrix_subtract(a, b):
    #global strassen_addition
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise Exception("Matrices have different size cannot subtract")
    result = [[a[i][j] - b[i][j]  for j in range(len(a[0]))] for i in range(len(a))]
    #strassen_addition += len(a)**2
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
    #prunes the padded rows and cols
    result = result[:rowmax]
    for i in range(len(result)):
        result[i] = result[i][:colmax]
    return result

def strassen_matrix_multiply(a, b):
    #global strassen_addition, strassen_multiply
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

    #strassen_multiply += 7
    #strassen_addition += 18

    result = []
    for i in range(len(c11)):
        result.append(c11[i] + c12[i])
    for j in range(len(c21)):
        result.append(c21[j] + c22[j])
    return result

'''
n = 2**10
a = np.ndarray.tolist(np.random.uniform(low=-1, high=1, size=(n,n)))
b = np.ndarray.tolist(np.random.uniform(low=-1, high=1, size=(n,n)))

start_time = time.time()
naive_matrix_multiply(a,b)
print("My program took " + str(time.time() - start_time) + " to run")
print("It took my naive method " + str(naive_addition) + " additions and " + str(naive_multiply) + " multiplications for a matrix of 2^10")
start_time = time.time()
strassen_matrix_multiply_helper(a,b)
print("My program took " + str(time.time() - start_time) + " to run")
print("It took my strassen method " + str(strassen_addition) + " additions and " + str(strassen_multiply) + " multiplications for a matrix of 2^10")
'''
n = 2**12
a = np.random.uniform(low=-1, high=1, size=(n,n))
b = np.random.uniform(low=-1, high=1, size=(n,n))
naive_addition = 0
naive_multiply = 0
strassen_addition = 0
strassen_multiply = 0
start_time = time.time()
naive_matrix_multiply(a,b)
print("My program took " + str(time.time() - start_time) + " to run")
print("It took my naive method " + str(naive_addition) + " additions and " + str(naive_multiply) + " multiplications for a matrix of 2^12")
start_time = time.time()
strassen_matrix_multiply_helper(a,b)
print("My program took " + str(time.time() - start_time) + " to run")
print("It took my strassen method " + str(strassen_addition) + " additions and " + str(strassen_multiply) + " multiplications for a matrix of 2^12")
