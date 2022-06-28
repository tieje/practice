# [LeetCode Problems](https://leetcode.com/)

I will not be writing my code for leetcode problems here.
I'll be writing it in my notebook first and then on the website itself.

## [Data Structures Study Plan](https://leetcode.com/study-plan/data-structure/?progress=vzfsoxj)

## [Algorithm Study Plan](#)

## Conclusion For Now

I'm not allowed to see the solution without a premium subscription.

Personally, I don't think it's worth it to buy the leetcode subscription because I won't have access to it later if I need it. We'll see about my dedication through studying Techlead problems.

## 5/5/2022

Buenos dias, I have returned.
I have decided to study algorithm questions and leetcode problems.
- skip
    - any problem that does not have a solution
    - hard problems (for now)

I'm going to keep all the solutions on the leetcode application for now.
Though I will use a white and pen for studying.
I'm not sure if I should go by the curated list for learning or the top interview questions.
I would like to use the curated list because it's mostly for people who are beginners.
But most of the problems are for premium users. Sheesh.

https://leetcode.com/problem-list/top-interview-questions/

My approach will be to:
1. Attempt the problem. Or at least think about how you would attempt the problem.
2. Look at the Solution. Try to understand internally.
3. Explain the problem to an empty chair.

Not all problems clearly indicate if the solution is free or not.
I'm going to go through all the tech lead problems first and get them down before I consider buying a leetcode subscription.

6/4/2022

I vastly prefer using leetcode for coding problems.
I prefer leetcode mostly because the code well-reviewed and the product is actually really good compared to techlead's problems.

6/4/2022

- [Began Data Structure I Study Plan](https://leetcode.com/study-plan/data-structure/?progress=6j9fx43)

6/5/2022

[88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
I was able to get the solution, but I did not use all of the variables presented to me.
My solution was Approach #1 with O(xlog(x)) time and O(n) space due to the built-in sort algorithm.
A better solution is to have two pointers, one for each array and increment them.
Approach 2 uses two pointers starting from the beginning, but it's actually a less understandable solution.
Approach 3 uses two pointers starting from the end. I had a good idea starting from the end.
range(start, stop, step)
Having the open space allows for copying the number to the end and not necessarily needing to worry about it ever.

6/6/2022

[350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)
I was able to get the two main solutions.
There was a third solution where you use the built-in method, which I could probably find in some python library.

[121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
I got the brute force method, which I knew was not correct.
I knew there should be some kind of single pass method, but I couldn't figure it out.
Or at least, I didn't think the initial solution in my head was correct because I felt like I had to try every possible combination.

6/14/2022

[566. Reshape the Matrix](https://leetcode.com/problems/reshape-the-matrix/)
I completed the brute force approach the first time through, but I'm sure there's a mathematical answer.
Interestingly enough, every approach will run O(m * n) time complexity and O(m * n) space complexity.
I don't think I will be doing this problem again, but it was fun to see that there are three different appraoches with the same outcome.

6/15/2022

[118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)
It turns out there was actually only one solution and I was pretty close.
1. Create a row of None with the appropriate amount of spots.
2. Fill in the ends first, then only deal with middle.
3. It's better to reference the existing triangle being built than referencing a prev row altogether.
It's still a double-for loop.

6/16/2022

[36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)
I did learn something really interesting about the python language.
[set() for _ in range(N)] will create a set() at each index that you can use the .add() method to add numbers to.
AND the numbers will never repeat because they're a set. Really interesting, but unfortunately, you need to figure out the magic formula first to the corrent index of the box.

6/17/2022

[74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

6/21/2022

[1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/solution/)
There was a much simpler solution that runs without allocating additional space, however, it was not functional so I wasn't a big fan of it. The function solution would have an additional O(n) space complexity instead of O(1). I'll need to keep this in mind when creating functional solutions for small problems.
[724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)
I messed up. I did not understand the problem properly. There is actually only one approach. It's pretty simple but it's a bit more mathematical. enumerate() in python is just a better range, honestly. I should use enumerate() more often. I didn't need to calculate for the right sum after all. I was pretty close even thought my solution was off.

6/26/2022

[205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)
I fundamentally misunderstood the problem. The problem is that each character is hard-mapped to another. I did not think of that way. I could have solved this problem pretty easily. I think it's worth doing again.



7/4/2022

- Redo [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

7/5/2022

- Get the best approach for [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

7/6/2022

- Get the best approach for [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

7/15/2022
- Redo [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)

7/16/2022
- Redo [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

7/21/2022
- Redo [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/solution/)
- Redo [724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)

7/26/2022
- Redo [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)

