def sum_of_3_5(num):
    total = 0
    for x in range (num):
        if x % 3 == 0 and x % 5 == 0:
            total += x
        elif x % 5 == 0:
            total += x
        elif x % 3 == 0:
            total += x
    return total

print(sum_of_3_5(1000))