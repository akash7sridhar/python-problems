def mutate_string(string, position, character):
    altered_string = string[:position] + character + string[position+1:]
    return altered_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)