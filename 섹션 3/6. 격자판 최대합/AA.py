import sys, os

root= "D:\\workspace\\Study\\파이썬 알고리즘 문제풀이(코딩테스트 대비)\\섹션 3"

sys.stdin=open(os.path.join(root, "6. 격자판 최대합\in0.txt"), "r")

n = int(input())
target_list = []

for i in range(0,n):
    target_list.append(list(map(int, input().split())))

for x in target_list:
    print(x)