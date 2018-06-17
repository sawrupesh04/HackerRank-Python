def swap_case(ss):
    if 1 <= len(ss) <= 1000:
        a = ''.join(map(str.swapcase, ss))
        return a


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
