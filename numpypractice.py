import numpy as np
data = np.array([10, 20, 30, 40, 50])
print(data[0])

import numpy as np
data = np.array([10, 20, 30, 40, 50])
print(data[-1])

import numpy as np
data = np.array([10, 20, 30, 40, 50])
print(data[2])

import numpy as np
data = np.array([10, 20, 30, 40, 50])
print(data[0:3])

import numpy as np
data = np.array([10, 20, 30, 40, 50])
print(data[1:4])

import numpy as np
data = np.array([10, 20, 30, 40, 50])
print(data[0:5:2])

import numpy as np
numbers = np.array([10, 25, 30, 15, 40, 5])
print(numbers[numbers > 25])

import numpy as np
numbers = np.array([11, 20, 33, 42, 55, 60])
print(numbers[numbers % 2 == 0])

import numpy as np
numbers = np.array([-10, 5, -3, 8, -7, 12])
print(numbers[numbers < 0])

import numpy as np
scores = np.array([35, 60, 75, 45, 90, 55])
addition = np.add(scores + 50,scores < 300)
print(addition)

import numpy as np
numbers = np.array([5, 15, 25, 35, 45, 55])
count = np.sum(numbers > 30)
print(count)

import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(data[1])

import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(data[:,0])

import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(data[1,2])

import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(data[0])
print(data[1])
print(data[:,1])
print(data[:,2])

import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(data[:,0])
print(data[:,2])

import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(data[data > 50])