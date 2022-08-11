import numpy as np
import matplotlib.pyplot as plt

N = 3
ind = np.arange(N)
width = 0.25

bvals = [0.02, 0.22, 0.59]
bar1 = plt.bar(ind, bvals, width, color = 'r')

ivals = [0.55, 1.22, 1.59]
bar2 = plt.bar(ind+width, ivals, width, color='g')

jvals = [1.25, 2.33, 1.25]
bar3 = plt.bar(ind+width*2, jvals, width, color = 'b')

plt.xlabel("Countries")
plt.ylabel("Categories")
plt.title("Single, Married and divorced ratio between 3 Countries")

plt.xticks(ind+width,['Bangladesh', 'India', 'Japan'])
plt.legend( (bar1, bar2, bar3), ('Divorced', 'Married', 'Single') )
plt.show()
