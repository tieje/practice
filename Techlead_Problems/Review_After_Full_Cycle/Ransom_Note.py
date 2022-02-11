#!/usr/bin/env python3
'''
https://www.techseries.dev/products/coderpro/categories/1831147/posts/6231429
Write a function that returns a Bool
canSpell(mag, word):
mag = ['a', 'b', 'c']
word = 'Bed'

my solution
'''
from collections import defaultdict


class Solution:
    def canSpell(self, mag, word):
        letterDict = defaultdict(int)
        for letter in mag:
            letterDict[letter] += 1
        for char in word:
            if letterDict[char] <= 0:
                return False
            letterDict[char] -= 1
        return True


print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
# True

print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
# False

'''
My solution works correctly the first time around.
My solution is exactly the same as the TechLead's solution.
I'm glad I've remembered defaultdict().
'''
