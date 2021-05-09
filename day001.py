import numpy as np
# a=np.arange(15).reshape(3, 5)
# print(a)
# print(type(a))
# print(a.ndim) #陣列有多少維度
# print(a.shape) #每個維度的大小
# print(a.size) #陣列當中有幾個元素
# print(a.dtype) #陣列中的資料型態
# print(a.itemsize) #陣列中每個元素佔用的空間
# print(a.data) #陣列所存在記憶體的位置
# print("list(a):", list(a))
# print("tolist", a.tolist())

a=np.random.randint(10, size=6)
print(a)
print(type(a))
print(a.ndim) #陣列有多少維度
print(a.shape) #每個維度的大小
print(a.size) #陣列當中有幾個元素
print(a.dtype) #陣列中的資料型態
print(a.itemsize) #陣列中每個元素佔用的空間
print("===================================")

b=np.random.randint(10, size=(3,4))
print(b)
print(type(b))
print(b.ndim) #陣列有多少維度
print(b.shape) #每個維度的大小
print(b.size) #陣列當中有幾個元素
print(b.dtype) #陣列中的資料型態
print(b.itemsize) #陣列中每個元素佔用的空間
print(b.data) #陣列所存在記憶體的位置
print("===================================")

c=np.random.randint(10, size=(2,3,2))
print(c)
print(type(c))
print(c.ndim) #陣列有多少維度
print(c.shape) #每個維度的大小
print(c.size) #陣列當中有幾個元素
print(c.dtype) #陣列中的資料型態
print(c.itemsize) #陣列中每個元素佔用的空間
print(c.data) #陣列所存在記憶體的位置
