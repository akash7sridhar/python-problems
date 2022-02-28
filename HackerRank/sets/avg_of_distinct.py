def average(array):
    # your code goes here
    sum1 = set(array)
    return(format(sum(sum1)/len(sum1),'.3f'))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)