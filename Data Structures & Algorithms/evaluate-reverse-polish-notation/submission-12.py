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
                print(op2, i, result, end=": ")
                if i == "+":
                    result += op2
                elif i == "-":
                    result = result - op2
                elif i == "*":
                    result = result * op2
                elif i == "/":
                    if result == 0:
                        result = 0
                    else:
                        result = op2 / result
                print(result)

        if (result-int(result)<0.5):
            return int(result)
        else:
            return int(result)+1
        