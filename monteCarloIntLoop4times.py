import numpy as np
import matplotlib.pyplot as plt
import random




N = []
for i in range(2,7):
    N = N + [int(10.0**i)]
    N = N + [int(2.0 * 10.0 ** i)]
    N = N + [int(4.0 * 10.0 ** i)]
    N = N + [int(6.0 * 10.0 ** i)]
    N = N + [int(8.0 * 10.0 ** i)]

inCircle = np.zeros(len(N),int)
pi_comp = np.zeros(len(N),float)
pi_diff = np.zeros(len(N),float)
for i in range(0,len(N)):
    for j in range(N[i]):
        point = (random.random() , random.random())
        r = point[0] * point[0] + point[1] * point[1]
        if r < 1.0:
            inCircle[i] = inCircle[i] + 1
    pi_comp[i] = float(inCircle[i])/float(N[i])
    pi_comp[i] = 4.0 * pi_comp[i]
    pi_diff[i] = np.pi - pi_comp[i]

print(pi_comp)
print(pi_diff)
print(N)
plt.plot(N,pi_comp,'-s')
plt.title('stochastic estimate of Pi with Monte Carlo integration')
plt.ylabel('Pi')
plt.xlabel('N')
plt.xscale('log')
plt.savefig('stocasticPiEstimation.png')
plt.show()