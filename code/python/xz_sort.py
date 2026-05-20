import random_num
import time

groups_num=int(input("input:"))

print("Selection Sort: A total of {} groups will be sorted.Data size:{}".format(groups_num,int(100*(groups_num+1)*groups_num/2)))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

for num in range(1,groups_num+1):
    randlist=random_num.get_random_num(1,100,100*num)
    
    list_len=len(randlist)
    start_time=random_num.get_time()
    
    for i in range(list_len-1):
        min_index=i
        for j in range(i+1,list_len):
            if randlist[j]<randlist[min_index]:
                min_index=j
        if min_index!=i:
            randlist[i],randlist[min_index]=randlist[min_index],randlist[i]

    end_time=random_num.get_time()
    

    
    
    print("Group "+str(num)+" Data Size:"+str(100*num)+" Time: "+str((end_time-start_time)*1000)+"ms.")
    
