# Python list — needs a loop (slow)
# bills = [5000, 1200, 9000, 800, 12000]
# taxed = [b*1.1 for b in bills]
# print(taxed)

import numpy as np
# NumPy array — one operation on all elements at once (fast)
bills = np.array([5000,12000,9000,8000,14000])
# ages = np.array([23,28,32,44,39])
# print(bills.dtype) #for printing data type
# print(bills.shape) # mean one dimenions, 5 elements
# print(bills.ndim)

# float_type = np.array([2000, 9000], dtype=np.float64)
# print(float_type)

# 2D Array - a table (rows * colums)
# patient table with 4 pateints and  column each
# patient_table = np.array(
#     [
#     [1, 23, 8000], #id, age , bill
#     [2, 24, 9000],
#     [3, 26, 23000],
#     [4, 28, 12000]]
# )
# print(patient_table.shape)
# print(patient_table[0])
# print(patient_table[:, 2])
# print(patient_table[1,2])
# print(patient_table[2,1])

print(bills[0])
print(bills[-1])
print(bills[1:4])
print(bills[:3])
print(bills[::2])

high = bills[bills>5000]
print(high)
print(bills[[0,2,4]])