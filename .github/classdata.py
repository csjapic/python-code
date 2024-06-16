import pandas as pd
import matplotlib.pyplot as plt

file = r'C:\Users\csjap\Downloads\MSDS-Orientation-Computer-Survey(in).csv'
dat = pd.read_csv(file)

dat['CPU_Cores'] = pd.to_numeric(dat['CPU Number of Cores (int)'], errors='coerce')
dat['RAM_GB'] = pd.to_numeric(dat['RAM (in GB)'], errors='coerce')
dat['Operating_System'] = dat['Operating System'].astype('category')

# Handle any missing values if needed
dat.dropna(subset=['CPU_Cores', 'RAM_GB'], inplace=True)

#Plot for CPU Cores
plt.figure(figsize=(10, 5))
plt.hist(dat['CPU_Cores'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.title('Distribution of CPU Cores')
plt.xlabel('Number of CPU Cores')
plt.ylabel('Frequency')
plt.savefig('cpu_cores_histogram.png')
plt.show()

#Plot for RAM in GB
plt.figure(figsize=(10, 5))
plt.hist(dat['RAM_GB'], bins=10, color='green', edgecolor='black', alpha=0.7)
plt.title('Distribution of RAM (GB)')
plt.xlabel('RAM (GB)')
plt.ylabel('Frequency')
plt.savefig('ram_histogram.png')
plt.show()

# Qualitative description of the Operating System feature
os_counts = dat['Operating_System'].value_counts()
print("Operating System Distribution:")
print(os_counts)

