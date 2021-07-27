import sys, os
import time
# root= "D:\\workspace\\Study\\파이썬 알고리즘 문제풀이\\Python_Algorithm\\Inflearn\\섹션 3"

# sys.stdin=open(os.path.join(root, "11. 격자판 회문수\in1.txt"), "r")

target_list = []
offset = 5
count = 0

for i in range(0,7):
    target_list.append(list(map(int, input().split())))

for i in range(0,7):
    
    for j in range(0,3):
        temp = []
        
        for k in range(0,offset):
            temp.append(target_list[i][j+k])

        if temp == temp[::-1]:
            count += 1

for i in range(0,7):
    
    for j in range(0,3):
        temp = []
        
        for k in range(0,offset):
            temp.append(target_list[j+k][i])

        if temp == temp[::-1]:
            count += 1

print(count)
