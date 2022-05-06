#!/usr/bin/python3
'''
Find the Kth largest element in a list.
There are several ways to do this supposedly.
Strat 1
Sort the list and pick the -k index from the
list.
Strat 2
Remove the maximum number from the list k times.
(probably the worst method)
Strat 3
There has to be a way to do without sorting...
It's possible to do it in one for loop where
we check how many numbers are bigger.
We need to test for median as well.
Decision
I'm just going to sort the list and pick the -k index.
Sorting is n*log(n) time. Choosing new maximum is n*log(n)
'''
import random
import heapq


class Solution:
    def kth_Largest(self, arr, k):
        sorted_arr = sorted(arr)
        return(sorted_arr[-k])


'''
a = [3, 5, 2, 4, 6, 8]
k = 3
print(Solution().kth_Largest(a, k))
# 5
The solution works. It's difficult for me to
think of a faster and more concise solution than this.
Time complexity is n*log(n) for sorting.
There is one important optimization though:
It's possible to sort it yourself and check if there
are numbers left to sort that is equivalent to k. This
small optimization is slightly faster, but with the
same worst-case scenario and possibly less clarity.
https://www.techseries.dev/products/coderpro/categories/1831147/posts/6190177
Solution: Use a heap
Can construct the heap in linear time.
Pop off k elements. log(n) time
k*log(n) time
Addition Solution: Quick select (similar to quick sort)
Partitioning algorithm that will divide an array by linear time.
Pick a pivot value.
Swap two numbers.
O(2n) ~ O(n) -- a bit complicated to implement
'''

# Solutions

# my solution done better: n*log(n) time


def findKthLargest(nums, k):
    return sorted(nums)[len(nums) - k]

# the best solution: k*log(n) time


def findKthLargest2(nums, k):
    return heapq.nlargest(k, nums)[-1]

# the best solution if you need to run AFAP, as fast as possible


def findKthLargest3(nums, k):
    def select(list, l, r, index):
        if l == r:
            return list[l]
        pivot_index = random.randint(l, r)
        # move pivot to the beginning of list
        list[l], list[pivot_index] = list[pivot_index], list[l]
        # partition
        i = l
        for j in range(l + 1, r + 1):
            if list[j] < list[l]:
                i += 1
                list[i], list[j] = list[j], list[i]
        # move pivot to the correct location
        list[i], list[l] = list[l], list[i]
        # recursively partition one side
        if index == i:
            return list[i]
        elif index < i:
            return select(list, l, i - 1, index)
        else:
            return select(list, i + 1, r, index)
    return select(nums, 0, len(nums) - 1, len(nums) - k)


print(findKthLargest3([3, 5, 2, 4, 6, 8], 3))
# 5
