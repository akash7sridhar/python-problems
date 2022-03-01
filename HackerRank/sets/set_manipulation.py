# Enter your code here. Read input from STDIN. Print output to STDOUT
A_n = int(input())
A_l = list(map(int, input().split()))
A = set(A_l)
n = int(input())
for i in range(n):
    b,c = map(str,input().split())
    if b == 'intersection_update':
        b_list = list(map(int,input().split()))
        b_set = set(b_list)
        A.intersection_update(b_set)
    elif b == 'update':
        b_list = list(map(int,input().split()))
        b_set = set(b_list)
        A.update(b_set)
    elif b == 'symmetric_difference_update':
        b_list = list(map(int,input().split()))
        b_set = set(b_list)
        A.symmetric_difference_update(b_set)
    elif b == 'difference_update':
        b_list = list(map(int,input().split()))
        b_set = set(b_list)
        A.difference_update(b_set)

print(sum(A))