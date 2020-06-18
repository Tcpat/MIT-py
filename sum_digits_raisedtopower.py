def i_to_number(x):
    string = str(x)
    lol = 0
    for num in range(0, len(string)):
        lol += int(string[num])**(num+1)
    return lol


def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    sum = 0
    result = []
    for i in range(a, b+1):
        if i < 10:
            result.append(i)
        else:
            if i_to_number(i) == i:
                result.append(i)
    return result
