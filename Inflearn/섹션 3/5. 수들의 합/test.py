import sys, os

target_list = [1,2,3,4,5]

def move (target_list, n):
    
    temp_list = target_list[:]

    for i in range(1, len(target_list)):
        target_list[i] = temp_list[i-1]
    
    target_list[0] = temp_list[-1]
    
    return target_list

print(move(target_list,5))
print(move(target_list,5))
