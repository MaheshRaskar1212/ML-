import numpy as np
x = np.array([
    [1200,4,10],
    [1000,5,9],
    [1000,1,4],
    [1000,5,15],
    [1000,3,10],
    [1000,2,13],
    
])

y = np.array([
    20,
    50,
    77,
    34,
    15,
    34
])
print("Number of Houses",len(x))
print("Number of features",len(x[1]))
print("Shape of x",np.shape(x))
print("Avg of house price",np.average(y))
print("max house price",np.max(y))
print("min house price",np.min(y))
print("std of area",np.std(x[1]))

print("All house areas",x[:,0])
print("All bedroom count",x[:,1])
print("First House",x[0])
print("First House",x[-1])
print("Age of 3rd house",x[2,2])

print("Std area", np.std)

area = x[:,0]
print(area)
mean = np.mean(area)
std = np.std(area)
z = (area - mean)/std
print("Std area", z)