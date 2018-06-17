if __name__ == '__main__':
    score_list = {}
    n = int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        if score in score_list:
            score_list[score].append(name)
        else:
            score_list[score] = [name]
        print(score_list)

    new_list = []
    for i in score_list:
        new_list.append([i, score_list[i]])
    new_list.sort()
    result = new_list[1][1]
    result.sort()
    print(*result, sep="\n")
