# For example if N = 4 then stair pattern will be like:

# *
# **
# ***
# ****

N = int(input())
for i in range(0, N):
    for j in range(0, i+1):
        print("*", end="")
    print()