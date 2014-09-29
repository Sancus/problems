# Determine whether a string is composed solely of unique characters or not.

def unique_n2(str1):
    for a in chars:
        matches = 0
        for b in chars:
            if a == b:
                matches += 1
        if matches > 1:
            return False
    return True

def unique(str1):
    unique = set()
    for a in str1:
        if a in unique:
            return False
        unique.add(a)
    return True

def unique_python(str1):
    if len(str1) == len(set(str1)):
        return True
    return False

print 'O(n^2) implementation'
print unique_n2('abcde')
print unique_n2('abccde')
print 'Pythonic implementation'
print unique_python('abcde')
print unique_python('abcdde')
print 'O(n) implementation'
print unique('abcde')
print unique('abcdde')

