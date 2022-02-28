# Enter your code here. Read input from STDIN. Print output to STDOUT

#input
M=int(input())
m=input()
N=int(input())
n=input()

#splitting and mapping(string to int_list)
x=list(map(int,m.split()))
y=list(map(int,n.split()))

#creation of sets
a=set(x)
b=set(y)

#difference in each sets
c=a.difference(b)
d=b.difference(a)

#union of difference
e=c.union(d)

#converting set to a list
result=list(e)

#sorting
result.sort()

#iteration
for i in range(len(result)):
    print(result[i])