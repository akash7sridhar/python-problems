# * 
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    N = int(input())
    for i in range(1,N+1):
        print("*"*i)
    for j in range(N-1,0,-1):
        print("*"*j)

    return 0


if __name__ == '__main__':
    main()