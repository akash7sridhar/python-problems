#    *
#   ***
#  *****
# *******
N = 4
for k in range(0,N):
    for l in range(0,N*2):
        if(l in range(N-k,N+k+1)):
            print("*", end="")
        else:
            print("",end=" ")
    print()