# 1 2 3 4
# 1 2 3
# 1 2
# 1

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    for i in range(N,0,-1):
        print(' '.join(str(e) for e in range(1, i + 1)))
    return 0

if __name__ == '__main__':
    main()