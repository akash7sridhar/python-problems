def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = input()
    rev = A[::-1]
    if A == rev:
        print("Yes")
    else:
        print("No")

    return 0

if __name__ == '__main__':
    main()