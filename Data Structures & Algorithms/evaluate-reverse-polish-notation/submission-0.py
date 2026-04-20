class Solution:

    def perform_operation(self, operation_str: str, operand1: str, operand2: str) -> int:
        operand1 = int(operand1)
        operand2 = int(operand2)
        match operation_str:
            case "+":
                return operand1 + operand2
            case "-":
                return operand1 - operand2
            case "*":
                return operand1 * operand2
            case "/":
                return operand1 / operand2
            case _:
                return operation_str

    def evalRPN(self, tokens: List[str]) -> int:
        # First operation:
        res = self.perform_operation(tokens[2], tokens[0], tokens[1])

        for i in range(3, len(tokens), 2):
            res = self.perform_operation(tokens[i+1], res, tokens[i])
        
        return res
