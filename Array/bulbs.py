A = [0, 1, 0, 1]
min_number = 0
switch = 0

for i in range(len(A)):
    if A[i] == switch:
        min_number += 1
        print(i)
        if switch == 0:
            switch = 1
        else:
            switch = 0
print(min_number)