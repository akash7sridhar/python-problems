# Given an integer N, print the corresponding pattern for N.

# For example if N = 4 then pattern will be like:
# A
# B B
# C C C
# D D D D
N = int(input("Enter your input: "))
pos = 1
for i in range(N):
    for j in range(i+1):
        character = chr(pos)
        print(character, end="")
    pos += 1
    print()