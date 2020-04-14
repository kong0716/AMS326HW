# Darren Kong
# 110770716
# AMS326 Midterm 2
import math
import matplotlib.pyplot as plt


def f(x, y):
    return x+y+(x*y)

#Runge Kutta Method
def runge_kutta(f, x0, y0, h):
    k1 = f(x0, y0)
    k2 = f(x0 + (.5*h), y0 + (.5*h*k1))
    k3 = f(x0 + (.5*h), y0 + (.5*h*k2))
    k4 = f(x0 + h, y0 + (h*k3))
    tn1 = x0 + h
    yn1 = y0 + ((1/6)*h*(k1 + k2 + k3 + k4))
    return tn1 , yn1

def problem2(x0, y0, h, max):
    xplot = list()
    yplot = list()
    x = x0
    y = y0
    h = .01
    while x <= max:
        xplot.append(x)
        yplot.append(y)
        x, y = runge_kutta(f, x, y, h)
        x = round(x, 2)
    return xplot, yplot

xplot, yplot = problem2(0, 1, .01, .5)
#print(xplot)
#print(yplot)
interpolatex = [.1, .2, .3, .4, .5]
interpolatey = list()
for x in interpolatex:
    interpolatey.append(yplot[xplot.index(x)])
#print(interpolatey)

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

def create_interpolant_matrix(Ys, Xs):
    m = [[0 for i in range(len(Xs))] for j in range(len(Xs))]
    for i in range(len(Xs)):
        for j in range(len(Xs)):
            # Needs to be in the correct row column template
            m[i][len(Xs)-1-j] = math.pow(Xs[i], j)
        #print(Xs[i]-1)
        m[i].append(Ys[i])
    #print(m)
    return m

a_coef = gauss_elimination(create_interpolant_matrix(interpolatey, interpolatex))

#print("ACoefficients " + str(a_coef))

def p_x(a_coef, x):
    val = 0
    for i in range(0, len(a_coef)):
        val += a_coef[i]*(x**(len(a_coef)-1-i))
    return val

poly_y = list()
for x in xplot:
    poly_y.append(p_x(a_coef, x))

plt.plot(xplot, poly_y, color='red')
plt.scatter(xplot, yplot)
plt.title("Midterm 2 Problem 2")
plt.xlabel('X-Values')
plt.ylabel('Y-Values')
plt.show()