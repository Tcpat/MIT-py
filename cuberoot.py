x = -33
epsilon = 0.01
high = abs(x)
low = 1.0
guess = 0.0
ans = (low + high)/2
while abs(ans**3 - abs(x)) >= epsilon:
    print("guess number: ", guess, "low is ", low, " and high is ", high)
    if ans**3 > abs(x):
        high = ans
        guess += 1
    elif ans**3 < abs(x):
        low = ans
        guess += 1
    ans = (low + high) / 2
if x < 0:
    ans = -ans
print("after ", guess, " guesses, the cube root of ", x, " is ", ans)
