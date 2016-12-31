
def  isPalindrome(s):
    list_s  = s.split()
    half = len(s) // 2
    end = len(s) - 1
    beginning = 0
    while half > 0:
        if list_s[beginning] == list_s[end]:
            beginning = beginning + 1
            end = end - 1
        else:
            return 'false'
    return 'true'
