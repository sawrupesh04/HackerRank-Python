def is_leap(year):
    leap = False

    if year>=1900 and year<=10**5:
        if year%4 == 0 and year%100 != 0 or year%400 == 0:
            return True
        return leap


n = int(input())
is_leap(n)
