#!/usr/bin/python3
'''
Given an array, find the three numbers that add up to zero.
Input:
[-1, 0, 1, 2, -4, -3]
Answer:
[[-1, 0, 1], [1, 2, -3]]

Initial Solution
A few common cases:
One negative number, one positive number, and zero.
The best the thing to do is probably to go one number at a time.
Unfortunately, going two numbers at a time requires a triple
for loop, which is way too much.
There are unique combinations of zero.
Sorting the list is probably best.
#1. Sort the list: either sorted or heapify.
#2. 

'''

def mysolution(arr):
    s_arr = sorted(arr)
    s_arr_len = len(s_arr) - 1
    if 0 in arr:
        zero_exists = True
    threesums = []
    for i in range(s_arr_len):
        bpt = s_arr[i]
        k = s_arr_len
        ept = s_arr[k]
        while bpt != 0 and ept >= 0:
            sum1 = bpt + ept
            if sum1 == 0 and zero_exists and ept != 0:
                threesums.append([bpt, 0, ept])
            elif sum1 > 0:
                plus = 1
                plusone = s_arr[i + plus]
                sum2 = sum1 + plusone
                while sum2 != 0 and plusone + i < s_arr_len:
                    plus += 1
                    plusone = s_arr[i + plus]
                    sum2 = sum1 + plusone
                if sum2 == 0:
                    threesums.append([bpt, plusone, ept])
            elif sum1 < 0:
                sub = 1
                minusone = s_arr[k - sub]
                sum2 = sum1 + minusone
                while sum2 != 0 and sub + k < s_arr_len:
                    print(minusone)
                    sub += 1
                    minusone = s_arr[k - sub]
                    sum2 = sum1 + minusone
                if sum2 == 0:
                    threesums.append([bpt, minusone, ept])
            k -= 1
            ept = s_arr[k]
    return(threesums)
'''
a = [-1, 0, 1, 2, -4, -3]
print(mysolution(a))
I could not figure it out, but I was able to visualize the solution
more easily so I guess that's improvement.
https://www.techseries.dev/products/coderpro/categories/1831147/posts/6228685
Actual Solutions
Brute Force
Go through every combination of triplets.
Triple for-loop - runs in O(n^3)
Can be reduced to two-some problem.
for n in numbs: 2sum(-n)
Best case is O(n^2) algorithm.

'''
