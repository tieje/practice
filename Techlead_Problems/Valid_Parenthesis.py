#!/usr/bin/python3
'''
Match Parentheses, {}, (), and [] in a string.
Return True if valid. Return False otherwise.
'''
from collections import defaultdict

def valid_parenthesis(string):
    '''
    Initial Strategy:
    Use the default dictionary to count parenthesis.
    If the number of opposing parenthesis is the same,
    return True. Return False otherwise.
    Revision 1
    Actually I need to look for the correct closing
    bracket as well. I need to do a test. The
    simplest solution for this is definitely recursive.
    Edge case 1
    If the string starts with a right bracket, it fails.
    Revision 2
    I need to categorize the brackets as either left or
    right closing brackets.
    '''
    p_dict = {
        'left': ['(', '[', '{'],
        'right': [')', ']', '}'],
        '(': ')',
        '[': ']',
        '{': '}'
    }
    p_string_dict = defaultdict(int)
    if string[0] in p_dict['right']:
        return False
    left = False
    for i in string:
        if left:
            if i in p_dict['right']:
                if i == p_dict[left]:
                    p_string_dict[left] -= 1
                else:
                    print('failed at i == p_dict[left]')
                    return False
        if i in p_dict['left']:
            left = i
            p_string_dict[i] += 1
    for k in p_string_dict.values():
        if k != 0:
            print('failed at final p_string_dict check')
            return False
    return True
'''
# Tests
a = '()({([])})'
b = '()(('
c = '(waeaf(awefew)wefawe)awefaef)'
d = '('
e = '()'
print(valid_parenthesis(d))
# False
print(valid_parenthesis(e))
# True
print(valid_parenthesis(a))
# True
print(valid_parenthesis(b))
# False
print(valid_parenthesis(c))
# False
'''
# I failed. Below is the actual solution:
