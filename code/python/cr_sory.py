import random_num
import time
from numba import jit


@jit(nopython=True)


def insertion_sort(randlist:list, list_len:int):
    for i in range(1, list_len):
        key = randlist[i]
        j = i - 1
        while j >= 0 and key < randlist[j]:
            randlist[j + 1] = randlist[j]
            j -= 1
        randlist[j + 1] = key





strat_group_num=int(input("input:"))
groups_num=int(input("input:"))

print("Insertion Sort: A total of {} groups will be sorted.Data size:{}".format(groups_num,100*(groups_num+1)*groups_num/2))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

for num in range(strat_group_num,groups_num+1):
    randlist=random_num.get_random_num(1,100,100*num)
    
    list_len=len(randlist)
    start_time=random_num.get_time()
    
    insertion_sort(randlist,list_len)
    

    end_time=random_num.get_time()
    print("Group "+str(num)+" Data Size:"+str(100*num)+" Time: "+str((end_time-start_time)*1000)+"ms.")
    
