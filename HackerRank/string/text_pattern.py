    # Size: 7 x 21 
    # ---------.|.---------
    # ------.|..|..|.------
    # ---.|..|..|..|..|.---
    # -------WELCOME-------
    # ---.|..|..|..|..|.---
    # ------.|..|..|.------
    # ---------.|.---------

# Enter your code here. Read input from STDIN. Print output to STDOUT
N,M = map(int,input().split())
c=".|."
for i in range(((N-1)//2)):
    print((c*i).rjust(M//2-1,'-')+c+(c*i).ljust(M//2-1,'-'))

for a in range(1):
    print("WELCOME".center(M,'-'))
    
for k in range(((N-1)//2)-1,0-1,-1):
    print((c*k).rjust(M//2-1,'-')+c+(c*k).ljust(M//2-1,'-'))
