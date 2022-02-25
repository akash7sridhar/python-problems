if __name__ == '__main__':
    students_list = []
    N = int(input())
    # Get Students in Nested
    for _ in range(N):
        name = input()
        score = float(input())
        students_list.append([name,score])
    students_list.sort(key = lambda x: x[1])
    print(students_list)
    # Finds Second Lowest Mark
    second_lowerst = []

    for i in range(N-1):
        if students_list[i][1] < students_list[i+1][1]:
            second_lowerst.append(students_list[i][1])
            print(students_list[i+1][1])
            break
    print(second_lowerst)
    second_lowerst_index = []
    # Find index where second Lowest Mark is Present
    
    for i in range(N-1):
        if students_list[1] == second_lowerst:
            # print(students_list[i][0])
            second_lowerst_index.append(students_list[i][0])
    print(second_lowerst_index)
    # Print Names of Second Lowest Mark
    for i in second_lowerst_index:
        print(students_list[i][0])