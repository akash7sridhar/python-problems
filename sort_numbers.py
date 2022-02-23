n = int(input("Enter No of element: "))
list = []
print("First list", list)
for i in range(1, n+1):
    i = int(input())
    list.append(i)
print("Before sort", list)
new_list = sorted(list)
print("after sort", new_list)