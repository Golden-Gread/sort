import random
import time
from numba import jit
import numpy as np

@jit(nopython=True)

def get_random_num(start:int, end:int, count:int)->list:
    ranum_list = []
    for i in range(0, count):
        ranum_list.append(random.randint(start, end))
    return ranum_list

def get_time():
    return time.time()

def swap(arr:list, i:int, j:int)->None:
    arr[i], arr[j] = arr[j], arr[i]
