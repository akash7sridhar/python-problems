def rangeSum(A, B):

    pre_sum = [0] * len(A)
    pre_sum[0] = A[0]

    for i in range(1, len(A)):
        pre_sum[i] = pre_sum[i -1] + A[i]
    pre_sum.insert(0,0)
    
    elements_sum = [0] * len(B)
    for i in range(0, len(B)):
        elements_sum[i] =  pre_sum[B[i][1] ] - pre_sum[B[i][0] - 1 ]
        # elements_sum[i] = i
    return(pre_sum)


A= [5, -2, 3 , 1, 2]
B = [[1,3], []]
print(rangeSum(A,B))

