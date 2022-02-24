# For example if N = 4 then stair pattern will be like:

#    *
#   **
#  ***
# ****
N = 4
for i in range(0, N):
    for j in range(1, N+1):
        if (N-i <= j):
            print("*", end="")
        else:
            print(" ", end="")
    print()
