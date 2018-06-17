def split_and_join(s):
    s = s.split(" ")
    a = "-".join(s)
    return a


if __name__ == '__main__':
    x = input()
    y = split_and_join(x)
    print(y)