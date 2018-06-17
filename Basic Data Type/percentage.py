if __name__ == '__main__':
    n = int(input())                                  # take input from user, how many give the name
    student_marks = {}                                # dictionary to store the student names and scores now it is empty
    for _ in range(n):                                # for the name and score
        name, *line = input().split()                 # take name and score white separator using split() method
        scores = list(map(float, line))               # pass each score as float by using map function
        student_marks[name] = scores                  # set the key and value of dictionary
    query_name = input()                              # take input from user to print the student average score
    query_score = student_marks[query_name]           # this statement select the name of the student from the dict
    print('{0:.2f}'.format(sum(query_score)/len(query_score))) # finally print the average of student with 2 decimal point
