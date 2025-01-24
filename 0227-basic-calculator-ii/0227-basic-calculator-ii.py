class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        stack, currNum, op = [], 0, "+"
        allOps = {"+", "-", "*", "/"}
        nums = set(str(x) for x in range(10))

        for i in range(len(s)):
            char = s[i]

            if char in nums:
                currNum = currNum * 10 + int(char)

            if char in allOps or i == len(s) - 1:
                if op == "+":
                    stack.append(currNum)
                elif op == "-":
                    stack.append(-currNum)
                elif op == "*":
                    stack[-1] *= currNum
                elif op == "/":
                    stack[-1] = int(stack[-1]/currNum)

                currNum = 0
                op = char
        return sum(stack)