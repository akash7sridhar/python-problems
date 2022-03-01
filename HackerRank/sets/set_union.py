# Enter your code here. Read input from STDIN. Print output to STDOUT
eng = int(input())
eng_roll = list(map(int, input().split()))

french = int(input())
french_roll = list(map(int, input().split()))

print(len(set(eng_roll).union(set(french_roll))))