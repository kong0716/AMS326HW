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

first45days = infectionsperday(.18, .08, 10, 45, 90)
next45days = infectionsperday(-.24, .04, first45days[44], 45, 90)
total90days = first45days + next45days[1:]
days = range(1, len(total90days)+1)

plt.bar(days, total90days)
plt.xticks(np.arange(0, 90, step=5))
plt.title("Infections Per Day For COVID-19")
plt.xlabel('Days')
plt.ylabel('Infected Individuals')
# Plot the distribution curve
plt.show()