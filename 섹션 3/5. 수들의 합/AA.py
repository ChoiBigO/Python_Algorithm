import sys, os

root= "D:\\workspace\\Study\\파이썬 알고리즘 문제풀이(코딩테스트 대비)\\섹션 3"

sys.stdin=open(os.path.join(root, "5. 수들의 합\in4.txt"), "r")

n,m = list(map(int, input().split()))
target_list = list(map(int, input().split()))

p1=0
p2=0

sum = 0

count = 0
i=0
while (p1<n and p2 <n):
    
    sum_value = sum(target_list[p1:p2+1])

    if sum_value == m:
        count += 1
        p1 += 1
    elif sum_value < m:
        p2 += 1
    elif sum_value > m:
        p1 += 1

    # print(sum_value)
    # print(f"p1 :{p1}")
    # print(f"p2 :{p2}")
    
# print(f"count : {count}")
# print("end")

print(count)
