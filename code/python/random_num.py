import random

def get_random_num(start:int, end:int, count:int)->list:
    ranum_list = []
    for i in range(0, count):
        ranum_list.append(random.randint(start, end))
    return ranum_list
