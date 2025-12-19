import numpy as np
import random
a=[]
for i in range(0,10):
    a.append(random.randint(0,100))
a=np.array(a)
print("Original array :",a)
print("sorted array  :  ",np.sort(a))
