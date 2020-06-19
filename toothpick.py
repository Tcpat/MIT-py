def toothpick(n):
    def toothpick1(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            power = 0
            while (n - 2 ** power) > 0:
                power += 1
            if n - 2 ** power == 0:
                return 2 ** power
            else:
                power -= 1
                i = n - 2 ** power
                return 2 * toothpick1(i) + toothpick1(i + 1)

    def totaltoothpick(n):
        total = 0
        for i in range(n):
            total += toothpick1(n - i)
        return total

    return totaltoothpick(n)
print(toothpick(23))
