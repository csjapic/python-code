import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

binom_dat = np.random.binomial(n=10, p=0.5, size=10000)
normal_dat = np.random.normal(loc=0, scale=1, size= 1000)
uniform_dat= np.random.uniform(low=0, high=1, size=1000)

plt.figure(figsize=(12,4))

#Binomial Distribution
plt.subplot(1,3,1)
plt.hist(binom_dat, bins =30, color = 'blue', edgecolor='black', alpha=0.7)
plt.title('Binomial Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

#Uniform Distribution
plt.subplot(1, 3, 3)
plt.hist(uniform_dat, bins=30, color='red', edgecolor='black', alpha=0.7)
plt.title('Uniform Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

#Normal Distribution
plt.subplot(1, 3, 2)
plt.hist(normal_dat, bins=30, color='green', edgecolor='black', alpha=0.7)
plt.title('Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')


plt.tight_layout()
plt.savefig('distributions_histograms.png')
plt.show()