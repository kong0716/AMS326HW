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
            y.append(math.ceil(y[i-1]*(1.0+dist[randint])))
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
        #print(Xs[i]-1)
        m[i].append(first45days[Xs[i]-1])
    print(m)
    return m

first45days = infectionsperday(.18, .08, 10, 45, 90)
next45days = infectionsperday(-.24, .04, first45days[44], 45, 90)
total90days = first45days + next45days[1:]  
days = range(1, len(total90days)+1)
a_coef = gauss_elimination(create_interpolant_matrix(first45days, [9, 18, 27, 36, 45]))
#print(a_coef)
def p_x(a_coef, x):
    val = 0
    for i in range(0, len(a_coef)):
        val += a_coef[i]*(x**(len(a_coef)-1-i))
    return val
#print(p_x(a_coef, 0.0))


def Kenny_Keepings(y, x):
    sumyi = 0
    sumxi = 0
    sumxisquared = 0
    sumxiXyi = 0
    for i in range(len(y)):
        sumyi += y[i]
        sumxi += x[i]
        sumxisquared += x[i]**2
        sumxiXyi += x[i]*y[i]
    a = ((sumyi*sumxisquared) - (sumxi*sumxiXyi))/((len(y)*sumxisquared) - (sumxi**2))
    b = ((len(y)*sumxiXyi) - (sumxi*sumyi))/((len(y)*sumxisquared) - (sumxi**2))
    return a, b
logy = list()
for i in range(0, len(next45days)):
    #print(next45days[i])
    logy.append(math.log(next45days[i]))
#print(logy)
a, b = Kenny_Keepings(logy, range(46, 91))
#print(a)
#print(b)
result1 = list()
for i in range(1, 46):
    result1.append(p_x(a_coef, i))
result2 = list()
for i in range(45, 90):
    result2.append((math.e**a)*(math.e**(b*i)))
#plt.plot(range(1,46), result1)
#plt.plot(range(46,91), result2)
plt.bar(days, total90days)
plt.xticks(np.arange(0, 90, step=5))
plt.title("Infections Per Day For COVID-19")
plt.xlabel('Days')
plt.ylabel('Infected Individuals')
# Plot the distribution curve
plt.show()