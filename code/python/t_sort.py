import random_num
import time
from numba import jit


@jit(nopython=True)


def Bucket_sort(arr:list, list_len:int):
    if not arr:
        return
    min_val = min(arr)
    max_val = max(arr)
    bucket = [0] * (max_val - min_val + 1)
    for num in arr:
        bucket[num - min_val] += 1
    idx = 0
    for i, count in enumerate(bucket):
        for _ in range(count):
            arr[idx] = i + min_val
            idx += 1
    





strat_group_num=int(input("input:"))
groups_num=int(input("input:"))

print("Bucket Sort: A total of {} groups will be sorted.Data size:{}".format(groups_num,100*(groups_num+1)*groups_num/2))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

for num in range(strat_group_num,groups_num+1):
    randlist=random_num.get_random_num(1,100,100*num)
    
    list_len=len(randlist)
    start_time=random_num.get_time()
    
    Bucket_sort(randlist,list_len)
    #print(randlist)

    end_time=random_num.get_time()
    print("Group "+str(num)+" Data Size:"+str(100*num)+" Time: "+str((end_time-start_time)*1000)+"ms.")
    
