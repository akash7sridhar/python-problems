# 0 0 0 0 1 0 0 0 0 
# 0 0 0 2 3 2 0 0 0 
# 0 0 3 4 5 4 3 0 0
# 0 4 5 6 7 6 5 4 0
# 5 6 7 8 9 8 7 6 5 

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    for i in range(0,N):
        count = 0
        count2 = 0
        for j in range(1,(N*2)):
            if(j >= N-i and j <= N ):
                print(i+count+1, end=" ")
                count2 = i+count+1
                count +=1
            elif(j > N and j <= N+i ):
                print(count2-1,end=" ")
                count2 = count2-1
            else:
                print("0",end=" ")
        print()



    return 0

if __name__ == '__main__':
    main()