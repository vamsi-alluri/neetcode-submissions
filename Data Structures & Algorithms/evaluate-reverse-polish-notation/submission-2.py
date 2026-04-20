class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        result = -1
        is_first_op = True
        for i in tokens:
            if i!="+" and i!="-" and i!="*" and i!="/":
                arr.append(int(i))
            else:
                if (is_first_op):
                    result = arr.pop()
                    is_first_op = False
                op2 = arr.pop()
                if i == "+":
                    result += op2
                elif i == "-":
                    result = op2 - result
                elif i == "*":
                    result = result * op2
                elif i == "/":
                    result = op2 // result

        return result 
        