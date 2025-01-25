class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        stack = []
        currNum = 0
        prevOp = '+'

        s += '+'
        for c in s:
            #if the character is not an operator
            if c.isdigit():
                currNum = currNum * 10 + int(c)
            elif c == ' ':
                continue


            #if the character is an operator
            else:
                if prevOp == '+':
                    stack.append(currNum)
                elif prevOp == '-':
                    stack.append(-currNum)
                elif prevOp == '*':
                    prevNum = stack.pop()
                    stack.append(prevNum * currNum)
                elif prevOp == '/':
                    prevNum = stack.pop()
                    stack.append(int(prevNum / currNum))

                currNum = 0
                prevOp = c
        return sum(stack)