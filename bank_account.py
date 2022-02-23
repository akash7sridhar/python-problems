def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    M = int(input())
    balance = N

    for i in range(M):
        A , B = map(int, input().split())
        if A == 1:
            balance = balance + B
            print(balance)
        elif A == 2:
            if ((balance - B) < 0):
                print("Insufficient Funds")
            else:
                balance = balance - B
                print(balance)
        

    return 0

if __name__ == '__main__':
    main()