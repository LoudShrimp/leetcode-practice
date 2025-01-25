class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        stack = []
        currNum = 0
        preOp = '+'

        s += '+'
        for c in s:
            if c.isdigit():
                currNum = currNum * 10 + int(c)
            elif c == ' ':
                continue

            else:
                if preOp == '+':
                    stack.append(currNum)
                elif preOp == '-':
                    stack.append(-currNum)
                elif preOp == '*':
                    prevNum = stack.pop()
                    stack.append(prevNum * currNum)
                elif preOp == '/':
                    prevNum = stack.pop()
                    stack.append(int(prevNum / currNum))
                currNum = 0
                preOp = c
        return sum(stack)
            