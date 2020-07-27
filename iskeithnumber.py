def is_keith_number(n):
    sum1 = 0
    if len(str(n)) <= 1:
        return False
    digits = []
    count = 0
    for i in range(len(str(n))):
        digits.append(int(str(n)[i]))
    while sum1 < n:
        sum1 = 0
        for i in range(count, len(digits)):
            sum1 += digits[i]
        digits.append(sum1)
        count += 1
    if sum1 == n:
        return count
    else:
        return False
