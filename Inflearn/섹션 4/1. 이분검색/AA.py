import sys, os
import time
# root= "D:\\workspace\\Study\\파이썬 알고리즘 문제풀이\\Python_Algorithm\\Inflearn\\섹션 4"

# sys.stdin=open(os.path.join(root, "1. 이분검색\in1.txt"), "r")

n,m = map(int, input().split())

target_list = list(map(int, input().split()))

target_list.sort()

p1 = 0
p2 = n-1

while(True):

    half = (p1+p2) // 2
    
    if m < target_list[half]:
        p2 = half
    elif m > target_list[half]:
        p1 = half
    else:
        print(half+1)
        break