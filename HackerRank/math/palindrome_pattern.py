# 1 
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1
N = int(input())
for i in range(1,N+1):
    print(((pow(10,i)-1) // 9) ** 2 )
