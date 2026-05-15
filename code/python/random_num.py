import random

def get_random_num(start, end):
    ranum_list = []
    for i in range(start, end+1):
        ranum_list.append(i)
    random.shuffle(ranum_list)
    return ranum_list
