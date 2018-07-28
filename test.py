import numpy as np
import random
def calc_pi(N):
    inCircle = 0
    for i in range(N):
        point = (random.random() , random.random())
        r = point[0]*point[0] + point[1]*point[1]
        if r < 1.0 :
            inCircle = inCircle +1
            # plt.plot(point[0], point[1], 'r.')
    # else:
    #     plt.plot(point[0], point[1], 'b.')
    res = float(inCircle)/float(N)
    res = 4.0*res
    return res

def pi_diff(temp_pi):
    return np.pi-temp_pi

def calc_pi_array(num_array):
    res_array = []
    for num in num_array:
        res_array = res_array + [calc_pi(num)]
    return res_array

Numbers = []
for i in range(2,7):
    Numbers = Numbers + [int(10.0**i)]
    Numbers = Numbers + [int(3.0 * 10.0 ** i)]
    Numbers = Numbers + [int(6.0 * 10.0 ** i)]

import matplotlib.pyplot as plt

for i in range(1,5):
    pis = calc_pi_array(Numbers)
    pi_diff_array = []
    for pi in pis:
        pi_diff_array = pi_diff_array + [pi_diff(pi)]
    print(Numbers)
    print(pis)
    print(pi_diff_array)
    plt.plot(Numbers,pi_diff_array,'-s')

plt.xscale('log')
plt.xlabel('N')
plt.ylabel('pi_calc - pi')
plt.savefig('PiDeviationFromTheExactValue.png')
plt.show()

#
# def double(x):
#     return 2.0*x
#
# def sinSquare(x):
#     return np.sin(x)*np.sin(x)
#
# print(double(3.0))
# print(sinSquare(np.pi/6.0))
