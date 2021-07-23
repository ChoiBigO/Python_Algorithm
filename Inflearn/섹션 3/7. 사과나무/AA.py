# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

import sys, os

# root= "D:\\workspace\\Study\\파이썬 알고리즘 문제풀이(코딩테스트 대비)\\섹션 3"

# sys.stdin=open(os.path.join(root, "7. 사과나무\in1.txt"), "r")

n=int(input())

blank = n//2

sum = 0

for i in range(0, n):

    target_list = list(map(int, input().split()))

    for j in range(blank, (n)- blank):
        sum += target_list[j]

    if i < n//2 :
        blank -= 1
    else:
        blank += 1
        

print(sum)
