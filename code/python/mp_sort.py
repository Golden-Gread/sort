import random_num
import time
groups_num=int(input("input:"))

print("Bubble Sort: A total of {} groups will be sorted.Data size:{}".format(groups_num,100*(groups_num+1)*groups_num/2))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

for num in range(1,groups_num+1):
    randlist=random_num.get_random_num(1,100,100*num)
    
    list_len=len(randlist)
    start_time=random_num.get_time()
    b=False
    while not b:
        b=True
        for i in range(list_len-1):
            if randlist[i]>randlist[i+1]:
                b=False
                randlist[i],randlist[i+1]=randlist[i+1],randlist[i]
    
    

    end_time=random_num.get_time()
    

    
    
    print("Group "+str(num)+" Data Size:"+str(100*num)+" Time: "+str((end_time-start_time)*1000)+"ms.")
    
