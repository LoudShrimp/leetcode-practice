class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        prevNum = currNum = result = 0
        prevOp = '+'

        s += 'e'
        for c in s:
            #check if the c is not an operator
            if c.isdigit():
                currNum = currNum * 10 + int(c)
            elif c == ' ':
                continue

            #check if the c is an operator
            else:
                if prevOp == '+':
                    result += currNum

                    prevNum = currNum
                if prevOp == '-':
                    result -= currNum

                    prevNum = -currNum
                if prevOp == '*':
                    result -= prevNum
                    result += prevNum * currNum
                    
                    prevNum = prevNum * currNum
                if prevOp == '/':
                    result -= prevNum
                    result += int(prevNum / currNum)

                    prevNum = int(prevNum / currNum)
                prevOp = c
                currNum = 0
        return result