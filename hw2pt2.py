import matplotlib.pyplot as plt
import numpy as np
import math

def infectionsperday(mu, sigma, initial, days, pool):
    #Generates 90 values that represent the percentage change using the normal distribution
    dist = np.random.normal(mu, sigma, pool)
    y = list()
    for i in range(0, days):
        if i == 0:
            y.append(initial)
        else:
            randint = np.random.randint(0, pool)
            y.append(math.floor(y[i-1]*(1.0+dist[randint])))
    return y

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

def create_interpolant_matrix(first45days, Xs):
    m = [[0 for i in range(len(Xs))] for j in range(len(Xs))]
    for i in range(len(Xs)):
        for j in range(len(Xs)):
            # Needs to be in the correct row column template
            m[i][len(Xs)-1-j] = math.pow(Xs[i], j)
        print(Xs[i]-1)
        m[i].append(first45days[Xs[i]-1])
    print(m)
    return m

first45days = infectionsperday(.18, .08, 10, 45, 90)
next45days = infectionsperday(-.24, .04, first45days[44], 45, 90)
total90days = first45days + next45days[1:]
days = range(1, len(total90days)+1)
a_coef = gauss_elimination(create_interpolant_matrix(first45days, [9, 18, 27, 36, 45]))
print(a_coef)
def p_x(a_coef, x):
    val = 0
    for i in range(0, len(a_coef)):
        val += a_coef[i]*(x**(len(a_coef)-1-i))
        print("x-value " + str(x))
        print("power " + str((len(a_coef)-1-i)))
        print(x**(len(a_coef)-1-i))
        #print(val)
    return val
print(p_x(a_coef, 0.0))
'''
result = list()
for i in range(0, 45):
    result.append(p_x(a_coef, i))
plt.plot(range(45), result)
plt.bar(days, total90days)
plt.xticks(np.arange(0, 90, step=5))
plt.title("Infections Per Day For COVID-19")
plt.xlabel('Days')
plt.ylabel('Infected Individuals')
# Plot the distribution curve
plt.show()
'''