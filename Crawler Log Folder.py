class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for char in logs:
            if char == "../" and not stack:
                continue 
            elif char == "../":
                stack.pop()
            elif char == "./":
                continue 
            else:
                stack.append(char)

        return len(stack)

