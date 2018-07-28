import numpy as np
import matplotlib.pyplot as plt
import random
N = 5000
inCircle = 0
for i in range(N):
    point = (random.random() , random.random())
    r = point[0]*point[0] + point[1]*point[1]
    if r < 1.0 :
        inCircle = inCircle +1
        plt.plot(point[0], point[1], 'r.')
    else:
        plt.plot(point[0], point[1], 'b.')
ans = float(inCircle)/float(N)
ans = 4.0*ans
plt.xlabel('x')
plt.ylabel('y')
plt.title('N= %s, N(inCircle)= %s'%(N,inCircle))
plt.savefig('MonteCarloIntegrationMethod.png')
plt.show()


# print(ans , np.pi , (np.pi-ans)/np.pi)




# x = random.uniform(0.0,1.0)
# y = random.uniform(0.0,1.0)

# plt.plot(x,y,'ro')
