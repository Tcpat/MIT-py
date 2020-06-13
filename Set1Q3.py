newstr = ""
longeststr = ""
s = 'abcbcdhjkl'

for i in range(len(s)):
    if i == 0:
        newstr += s[i]
    elif s[i] >= s[i - 1]:
        newstr += s[i]
    elif s[i] < s[i - 1]:
        if len(newstr) > len(longeststr):
            longeststr = newstr
        newstr = ""
        newstr += s[i]
    if i == len(s) - 1:
        if len(newstr) > len(longeststr):
                longeststr = newstr

print(longeststr)
