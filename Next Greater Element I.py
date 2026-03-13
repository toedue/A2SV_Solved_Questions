class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapping = dict()
        result = []

        for num in nums2:
            while stack and num > stack[-1]:
                mapping[stack.pop()] = num
            stack.append(num)

        while stack:
            mapping[stack.pop()] = -1


        for num in nums1:
            result.append(mapping[num])
            
        return result




"""
nums1 = [4,1,2], nums2 = [1,3,4,2]
For 1 → next greater is 3
For 3 → next greater is 4
For 4 → no next greater → -1
For 2 → no next greater → -1

stack helps us keep track of numbers whose “next greater element” we haven't found yet.

Goal: For each number, find the next greater number to its right.

Step 1 → Start with empty stack
stack = []
next_greater = {}

Step 2 → Read 1
stack = [1]
No one is greater than 1 yet, so we wait.

Step 3 → Read 3
Now check:
Is 3 > top of stack (1)?
✔ Yes! 3 is greater.
So, 3 is the next greater element of 1.

Write it:
next_greater[1] = 3

Pop 1 from stack:
stack = []

Now push 3:
stack = [3]

Step 4 → Read 4
Check:
Is 4 > 3?
✔ Yes → next greater for 3 is 4.
Write it:
next_greater[3] = 4

Pop 3:
stack = []

Push 4:
stack = [4]

Step 5 → Read 2
Check:
Is 2 > 4?
❌ No → do nothing.

Push 2:
stack = [4, 2]

End of nums2
Any number still in the stack has no next greater element.
So:
next_greater[4] = -1
next_greater[2] = -1

Now answer nums1 = [4,1,2]
Look up each one:
next_greater[4] = -1
next_greater[1] = 3
next_greater[2] = -1

So answer is:
[-1, 3, -1]






"""
