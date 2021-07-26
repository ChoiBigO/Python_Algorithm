import sys, os
import time
root= "D:\\workspace\\Study\\파이썬 알고리즘 문제풀이\\Python_Algorithm\\Inflearn\\섹션 3"

sys.stdin=open(os.path.join(root, "10. 스도쿠 검사\in0.txt"), "r")

target_list = []

check = 0
nine_list = [1,2,3,4,5,6,7,8,9]

for i in range(0,9):
    target_list.append(list(map(int, input().split())))

row_sum = [0]*9
col_sum = [0]*9
sec_sum = [[0 for x in range(0,9)] for a in range(0,3) ]

for i in range(0,9):

    for j in range(0,9):
        
        row_sum[j] = target_list[i][j]
        sec_sum[i%3][j%3] = target_list[i][j]       

    # Row Inspect
    row_sum.sort()
    if row_sum == nine_list:
        print("Same")
    else:
        check =1
        print("Row Inspect")
        break

if check == 1:
    print("NO")
else:
    print("YES")