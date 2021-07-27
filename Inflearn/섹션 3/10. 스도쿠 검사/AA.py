import sys, os
import time
# root= "D:\\workspace\\Study\\파이썬 알고리즘 문제풀이\\Python_Algorithm\\Inflearn\\섹션 3"

# sys.stdin=open(os.path.join(root, "10. 스도쿠 검사\in4.txt"), "r")

target_list = []

check = 0
ref_list = [1,2,3,4,5,6,7,8,9]

for i in range(0,9):
    target_list.append(list(map(int, input().split())))

row_list = [0]*9
col_list = [[0 for x in range(0,9)] for a in range(0,9) ]
sec_list = [[0 for x in range(0,9)] for a in range(0,3) ]

for i in range(0,9):

    for j in range(0,9):
        
        row_list[j] = target_list[i][j]
        sec_list[j//3][(i%3)*3+(j%3)] = target_list[i][j]       
        col_list[j][i] = target_list[i][j]

    # Row Inspect
    row_list.sort()
    if row_list != ref_list:
        check = 1
        break

    # Section Inspect
    if i%3 == 2:
        for x in sec_list:
            x.sort()
            if x != ref_list:
                check = 1
                break
        if check == 1 : break


for x in col_list:
    x.sort()
    if x != ref_list:
        check = 1
        break
    if check == 1: break

if check == 1:
    print("NO")
else:
    print("YES")