import numpy as np
a=np.arange(15).reshape(3,5)
print(a)

#陣列的常用屬性
print(a.dtype) #int32
print(a.itemsize) #4位元

# numpy中的型態判斷
print(a.dtype == 'int32')
print(a.dtype is "int32")
print(a.dtype is np.int32)

# 資料型態的正確用法
print(a.dtype == "int32")
print(a.dtype == np.int32)
print(a.dtype is np.dtype('int32'))


