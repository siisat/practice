# 202012503

# 3.3
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from ss_expsmoo import ss_expsmoo

def ss_expsmoo(x, alpha):
    if not hasattr(ss_expsmoo, "ynm1"):
        ss_expsmoo.ynm1 = 0.0
    
    y = (1 - alpha) * ss_expsmoo.ynm1 + alpha * x
    
    ss_expsmoo.ynm1 = y
    return y


data = loadmat('djia.mat')
x2003 = data['x2003'].flatten()
nsamp = len(x2003)

output = []
alpha = 0.1

if hasattr(ss_expsmoo, "ynm1"):
    del ss_expsmoo.ynm1

for n in range(nsamp):
    x = x2003[n]               
    y = ss_expsmoo(x, alpha)   
    output.append(y)           

plt.figure(figsize=(9, 5))
plt.plot(range(1, nsamp + 1), x2003, label="Original x2003 (DJIA)")
plt.plot(range(1, nsamp + 1), output, label="Exponential Smooth Output")

plt.axis([1, 252, 7500, 10500])
plt.title("Exponential Smoother Output for DJIA 2003")
plt.xlabel("Sample index (days)")
plt.ylabel("DJIA Value")
plt.legend()
plt.grid(True)
plt.show()


# 3.7
import numpy as np
import matplotlib.pyplot as plt
from ss_conv import ss_conv

def ss_conv(h, x, Nh, Nx):
    y = np.convolve(h, x)

    N_start = Nh + Nx            
    N_end = N_start + len(y) - 1 

    n = np.arange(N_start, N_end + 1)
    return y, n


h = np.array([4, 3, 2, 1])
x = np.array([-3, 7, 4])
Nh = 5 
Nx = 7 

y, n = ss_conv(h, x, Nh, Nx)

print("Convolution result:", y)
print("Index vector n:", n)

plt.figure(figsize=(8, 4))
plt.stem(n, y)
plt.title("Convolution result with proper indices")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid(True)
plt.show()
