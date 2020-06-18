def string_letter_count(s):
    letter = "abcdefghijklmnopqrstuvwxyz"
    freq = {}
    s = s.lower()
    result = ""
    for ch in letter:
        for i in s:
            if i == ch:
                if i in freq.keys():
                    freq[i] += 1
                else:
                    freq[i] = 1
    for i in freq.keys():
        result += str(freq[i]) + str(i)
    return result
