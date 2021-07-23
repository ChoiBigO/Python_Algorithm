import sys, os

# root= "D:\\workspace\\Study\\파이썬 알고리즘 문제풀이\\Python_Algorithm\\섹션 3"

# sys.stdin=open(os.path.join(root, "6. 격자판 최대합\in0.txt"), "r")

n = int(input())
target_list = []
result_list = []

for i in range(0,n):
    target_list.append(list(map(int, input().split())))

diagonal_sum = [0]*2 # 대각선 2개
col_sum = [0]*n # 5개 
row_sum = [0]*n # 5개

for i in range(0,n):
    for j in range(0,n):

        row_sum[i] += target_list[i][j]
        col_sum[j] += target_list[i][j]
        
        if i==j:
            diagonal_sum[0] += target_list[i][j]

        if (i+j) == n-1:
            diagonal_sum[1] += target_list[i][j]

result_list.extend(row_sum)
result_list.extend(col_sum)
result_list.extend(diagonal_sum)

print(max(result_list))
        
