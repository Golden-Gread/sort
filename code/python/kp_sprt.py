import random_num
import time
from numba import jit


@jit(nopython=True)

def partition(arr, low, high):
    """划分函数"""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

@jit(nopython=True)
def quick_sort_inplace(arr, low, high):
    """原地快速排序，更节省内存"""
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)





strat_group_num=int(input("input:"))
groups_num=int(input("input:"))

print("Quick Sort: A total of {} groups will be sorted.Data size:{}".format(groups_num,100*(groups_num+1)*groups_num/2))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

for num in range(strat_group_num,groups_num+1):
    randlist=random_num.get_random_num(1,100,100*num)
    
    list_len=len(randlist)
    start_time=random_num.get_time()
    
    quick_sort_inplace(randlist,0,list_len-1)
    

    end_time=random_num.get_time()
    print("Group "+str(num)+" Data Size:"+str(100*num)+" Time: "+str((end_time-start_time)*1000)+"ms.")
    
