import numpy as np
count = 1

a = 18
b = 32

a_list = []
b_list = []


while count <= 50:
    a_list.append(a * count)
    b_list.append(b * count)
    count += 1



 
def common_member(a, b):
    return list(np.intersect1d(a, b))


common_elements = common_member(a_list, b_list)
# common_elements = 175 // 35
print(common_elements)
# print(a_list)
