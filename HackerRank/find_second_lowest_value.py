# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
# Example
# The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:
# alpha
# beta

# Output Format
# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.
# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry

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