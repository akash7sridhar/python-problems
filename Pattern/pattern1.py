# Pattern With N input
# If N = 3
# ***
# ***
# ***
n = int(input("Enter value of N: "))
## Solution 1
print("Solution 1")
for i in range(n):
    print("*" * n)

## SOlution 2
print("Solution 2")
for i in range(0,n):
    for j in range(0, n):
        print("*", end='')
    print()

