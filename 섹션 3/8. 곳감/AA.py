import sys, os

# root= "D:\\workspace\\Study\\파이썬 알고리즘 문제풀이\\Python_Algorithm\\섹션 3"

# sys.stdin=open(os.path.join(root, "8. 곳감\in1.txt"), "r")


def right_move (target_list, n):
    
    temp_list = target_list[:]

    for i in range(1, len(target_list)):
        target_list[i] = temp_list[i-1]
    
    target_list[0] = temp_list[-1]
    
    return target_list

def left_move (target_list, n):
    
    temp_list = target_list[:]

    for i in range(0, len(target_list)-1):
        target_list[i] = temp_list[i+1]
    
    target_list[-1] = temp_list[0]
    
    return target_list

n = int(input())

target_list = []

for i in range(0,n):
    target_list.append(list(map(int, input().split())))
    

m = int(input())

for j in range(0,m):
    row,mode, count = list(map(int, input().split()))


    if mode == 0:
        for k in range(0,count):
            left_move(target_list[row-1], n)

    else:
        for k in range(0,count):
            right_move(target_list[row-1], n)


blank = -1
sum = 0

for a in range(0,n):
    
    if a <= n//2:
        blank += 1
    else :
        blank -=1

    for b in range(blank, n-blank):
        sum += target_list[a][b]

print(sum)
    