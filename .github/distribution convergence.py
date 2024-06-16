import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

n=1000
p=0.5

binom_dat = np.random.binomial(n=n, p=p, size=10000)

mean = n * p
st_dev = np.sqrt(n * p * (1-p))
norm_dat = np.random.normal(loc=mean, scale=st_dev, size=10000)


plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.hist(binom_dat, bins=50, color='blue', edgecolor='black', alpha=0.7)
plt.title('Binomial Distribution (n=1000, p=0.5)')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(norm_dat, bins=50, color='red', edgecolor='black', alpha=0.7)
plt.title('Normal Distribution (mean=500, std_dev=15.81)')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.savefig('binomial_normal_convergence.png')
plt.show()