import sys, os
import time
root= "D:\\workspace\\Study\\파이썬 알고리즘 문제풀이\\Python_Algorithm\\Inflearn\\섹션 4"

sys.stdin=open(os.path.join(root, "2. 랜선자르기\in0.txt"), "r")

k,n = map(int, input().split())

target_list = []

for i in range(0,k):
    target_list.extend(list(map(int, input().split())))

# print(f"k : {k} , n : {n}")
# print(target_list)

count = 0
lan_len = max(target_list)

while (lan_len > 0):

    # target_list = [x for x in target_list if x >= lan_len]

    temp_list = [x for x in target_list if x >= lan_len]

    # print(f"target_list : {temp_list} lan_len : {lan_len}")

    for x in temp_list:
        temp = x
        while (temp >= lan_len):
            temp -= lan_len
            count += 1
        
    if count >= n:
        print(lan_len)
        break
    else :
        count = 0
    
    lan_len -= 1
## test