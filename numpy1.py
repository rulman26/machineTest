import numpy as np
import time
SIZE=10
L1=range(SIZE)
L2=range(SIZE)
A1=np.arange(SIZE)
A2=np.arange(SIZE)
start=time.time()
print(L1)
print(L2)
result=[(x,y)for x,y in zip(L1,L2)]
print('Resultado es =>')
print(result)
print((time.time()-start)*1000)
print()
start=time.time()
print(A1)
print(A2)
result=A1+A2
print('Resultado es =>')
print(result)
print((time.time()-start)*1000)

