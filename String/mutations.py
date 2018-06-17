def mutation(string, position, character):
    Str = string[:position] + str(character) + string[position+1:]
    return Str


if __name__ == '__main__':
    s = input()
    p = int(input())
    c = input()
    result = mutation(s, p, c)
    print(result)