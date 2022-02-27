def print_formatted(number):
    # your code goes here
    formatted = []
    for i in range(1,number+1):
        formatted.append([format(i,'d'),format(i,'o'),format(i,'X'),format(i,'b')])
    for i in formatted:
        print(*(rep.rjust(len(formatted[-1][3])) for rep in i))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)