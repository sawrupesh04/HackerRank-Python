if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())  # create a list of items in given iterable

    # hash is fix integer that identifies a particular value
    print(hash(tuple(integer_list)))  # print the hash
