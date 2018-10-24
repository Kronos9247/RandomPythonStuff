import numpy as np
import scipy.special as sp

def rnum(n):
    if n == 0:
        return 4
    
    pre = rnum(n - 1)
    return np.power(2, sp.factorial(pre))

print(rnum(1))