if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ar = []                                 # create a list now it is empty
    p = 0                                   # set the position of the list value now position is 0

    for i in range(x+1):                    # set range of i by increment X by 1
        for j in range(y+1):                # Set range of j by increment y by 1
            for k in range(z+1):            # Same for k
                if i+j+k != n:             # now check the condition
                    ar.append([])           # append the list to ar
                    ar[p] = [i, j, k]       # add the value to the list ar
                    p += 1                  # increment position by 1
    print(ar)

