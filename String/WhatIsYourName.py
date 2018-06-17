def print_name(x, y):
    return "Hello {0} {1}! You just delved into python.".format(x, y)


if __name__ == "__main__":
    first_name = input()
    last_name = input()
    result = print_name(first_name, last_name)
    print(result)