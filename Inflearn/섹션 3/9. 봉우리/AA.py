import sys, os
import time
root= "D:\\workspace\\Study\\파이썬 알고리즘 문제풀이\\Python_Algorithm\\섹션 3"

sys.stdin=open(os.path.join(root, "9. 봉우리\in5.txt"), "r")

n = int(input())
target_list = []
count = 0

check = [[0 for col in range(n+2)] for row in range(n+2)]

temp = []
target_list.append([0]*(n+2))


for i in range(0,n):
    temp = [0]
    temp.extend(list(map(int, input().split())))
    temp.append(0)

    target_list.append(temp)

target_list.append([0]*(n+2))

start = time.time()

for i in range(1, n+1):
    for j in range(1, n+1):

        if check[i][j] == 0:

            if target_list[i-1][j] < target_list[i][j] :
                if target_list[i+1][j] < target_list[i][j] :
                    if target_list[i][j-1] < target_list[i][j]:
                        if target_list[i][j+1] < target_list[i][j]:
                            count += 1
                            check[i+1][j] = 1
                            check[i-1][j] = 1
                            check[i][j+1] = 1
                            check[i][j-1] = 1



print(count)
print("time :", time.time() - start)