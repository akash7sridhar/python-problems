# Enter your code here. Read input from STDIN. Print output to STDOUT
# Solution 1 
Solution = int(input("Enter Solution Number: "))
if Solution == 1:
    k = int(input())
    room = list(map(int, input().split()))
    room_set = set(room)
    captain = 0
    for i in room_set:
        count = 0
        for j in room:
            if i == j:
                count += 1
        if count < k:
            print(i)
            break

else:

    # Solution 2
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    k = int(input())
    room = list(map(int, input().split()))
    room_set_uniq = set()
    room_set = set()
    for i in room:
        if i in room_set_uniq:
            room_set.add(i)
        else:
            room_set_uniq.add(i)

    captain_room = room_set_uniq.difference(room_set)
    print(list(captain_room)[0])