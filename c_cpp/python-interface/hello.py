import time
import hello 
import numpy as np

limit = 5_000_000

start = time.time()
print(np.sum(np.arange(limit)))
print(f'{time.time() - start:.6} sec')

start = time.time()
hello.sum_a_list(limit)
print(f'{time.time() - start:.6} sec')