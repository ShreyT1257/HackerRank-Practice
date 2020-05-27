def is_leap(year):
    leap = True
    if(year%100 != 0) and (year%4 == 0) and (year%100 == 0):
        return leap
    else:
        return False

year=int(input())
print(is_leap(year))
