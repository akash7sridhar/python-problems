# *****
#  ****
#   ***
#    **
#     *

N = 5
for k in range(0,N):
    for l in range(0,N):
        if(k <= l):
            print("*", end="")
        else:
            print("",end=" ")
    print()