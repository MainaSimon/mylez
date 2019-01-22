def find_needle(haystack):
    for word in haystack:
        if word == 'needle':
            return "found the needle at position " + str(haystack.index('needle'))
