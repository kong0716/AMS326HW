import matplotlib.pyplot as plt

#Runge Kutta Method

def f(x, y):
    return x+y+(x*y)

def runge_kutta(f, x0, y0, h):
    k1 = f(x0, y0)
    k2 = f(x0 + (.5*h), y0 + (.5*h*k1))
    k3 = f(x0 + (.5*h), y0 + (.5*h*k2))
    k4 = f(x0 + h, y0 + (h*k3))
    tn1 = x0 + h
    yn1 = y0 + ((1/6)*h*(k1 + k2 + k3 + k4))
    return tn1 , yn1
xplot = list()
yplot = list()
x = 0
y = 1
h = .0001
while x < 2:
    xplot.append(x)
    yplot.append(y)
    x, y = runge_kutta(f, x, y, h)
plt.scatter(xplot, yplot)
plt.show()
'''
def g(k, A, T):
    return k*(A-(T**(.999)))

def runge_kutta(g, x0, y0, h, k):
    k1 = g(k, x0, y0)
    k2 = g(k, x0 + (.5*h), y0 + (.5*h*k1))
    k3 = g(k, x0 + (.5*h), y0 + (.5*h*k2))
    k4 = g(k, x0 + h, y0 + (h*k3))
    tn1 = x0 + h
    yn1 = y0 + ((1/6)*h*(k1 + k2 + k3 + k4))
    return tn1 , yn1

def findk(mins, maxs, increments, epsilon):
    b = increments
    xplot = list()
    yplot = list()
    while abs(maxs) - abs(mins) >= epsilon:
        xplot = list()
        yplot = list()
        x = 0
        y = 1
        h = .01
        #T_180 = 55.55
        b = (maxs + mins)/2
        while x < 180:
            xplot.append(x)
            yplot.append(y)
            x, y = runge_kutta(g, x, y, h, b)
        if yplot[len(yplot)-1] - 55.55 == 0:
            return b
        if yplot[len(yplot)-1] - 55.55 < epsilon:
            mins = b+increments
        if yplot[len(yplot)-1] - 55.55 > epsilon:
            maxs = b-increments
        print(b)
    plt.scatter(xplot, yplot)
    plt.show()
    return b

findk(0, 100, 10**(-10), 10**(-10))
'''