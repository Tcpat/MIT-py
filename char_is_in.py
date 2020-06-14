def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    if char == aStr[int(len(aStr)/2)]:
        return True
    elif char < aStr[int(len(aStr)/2)]:
        return isIn(char, aStr[0:int(len(aStr)/2)])
    elif char > aStr[int(len(aStr)/2)]:
        return isIn(char, aStr[int(len(aStr)/2):-1])
