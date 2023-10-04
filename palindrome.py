def isPalindromicNumber(something):
    something = str(something)

    if something == something[::-1]:
        return True
    return False


print(isPalindromicNumber(121))