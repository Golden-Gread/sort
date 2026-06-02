import random_num
import time
from numba import jit
import numpy as np

@jit(nopython=True)


def main(start_group:int, groups_num:int, num:int, randlist:list)->list:
    
    list_len=len(randlist)
    
    for i in range(list_len-1):
        min_index=i
        for j in range(i+1,list_len):
            if randlist[j]<randlist[min_index]:
                min_index=j
        if min_index!=i:
            randlist[i],randlist[min_index]=randlist[min_index],randlist[i]
    
    return [num]

        


start_group=int(input("input:"))
groups_num=int(input("input:"))
print("Selection Sort: A total of {} groups will be sorted.Data size:{}".format(groups_num,int(100*(groups_num+1)*groups_num/2)))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

for i in range(start_group,groups_num+1):
    randlist=random_num.get_random_num(1,10000,100*i)
    start_time=time.time()
    list1=main(start_group,groups_num,i,randlist)
    end_time=time.time()
    print("Group "+str(list1[0])+" Data Size:"+str(100*list1[0])+" Time: "+str((end_time-start_time)*1000)+"ms.")




