if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(arr)
    scores.sort()
    runner = 0
    for i in range(n, 0 , -1):
        if (scores[i-1] == scores[i-2]):
            runner = scores[i-3]
        elif (scores[i-1] > scores[i-2]):
            runner = scores[i-2]
            break
    print(runner)
