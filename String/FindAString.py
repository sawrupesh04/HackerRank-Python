def count_substring(a, b):
    counter = 0
    i = 0
    while i < len(a):
        if a.find(b, i) >= 0:
            i = a.find(b, i) + 1
            counter += 1
        else:
            break
    return counter



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
