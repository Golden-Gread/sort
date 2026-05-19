import random_num

groups_num=int(input("input:"))


for num in range(1,groups_num+1):
    randlist=random_num.get_random_num(1,100,100*num)
    f = open(".\\python_out\\mp_sor100t.out","a")
    start_time=random_num.get_time()

    for i in range(len(randlist)):
        for j in range(i+1,len(randlist)):
            if randlist[i]>randlist[j]:
                #temp=randlist[i]
                #randlist[i]=randlist[j]
                #randlist[j]=temp
                random_num.swap(randlist,i,j)

    end_time=random_num.get_time()
    
    f.write("Group "+str(num)+" Time: "+str((end_time-start_time)*1000)+"ms."+"\n")
    print("Group "+str(num)+" Time: "+str((end_time-start_time)*1000)+"ms.")
    f.close()
