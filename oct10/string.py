# Given two strings, determine whether one is a permutation of the other.

def perm(str1, str2):
    if len(str1) == len(str2):
        return True
    if sorted(str1) == sorted(str2):
        return True
    return False

if perm('dog', 'god'):
    if not perm('this is a test', 'this is a test a'):
        print 'Tests pass.'

