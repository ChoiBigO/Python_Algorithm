check = [[0]*7]*7
# check = [[0 for col in range(7)] for row in range(7)]
check[1][1] = 999

for x in check:
    print(x)