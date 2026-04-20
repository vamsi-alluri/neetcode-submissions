class Solution:

    # Recursive function: returns 
    def generate_parenthesis(self, parenthesis_str: str, open_count:int, close_count:int, n:int) -> List[str]:

        print(f"Open:{open_count}, Close {close_count}, n: {n}, Current Str: {parenthesis_str}")
        if (close_count > open_count):
            return []
        
        if (open_count + close_count >= n * 2):
            if (open_count == close_count):
                print(f"Checkpassed | Open:{open_count}, Close {close_count}, n: {n}, Current Str: {parenthesis_str}")    
                return [parenthesis_str]
            else:
                return []
     

        resultant_strings = self.generate_parenthesis(parenthesis_str + '(', open_count + 1, close_count, n)

        resultant_strings.extend(self.generate_parenthesis(parenthesis_str + ')', open_count, close_count + 1, n))

        print(resultant_strings)
        return resultant_strings

    def generateParenthesis(self, n: int) -> List[str]:

        open_count = 0
        close_count = 0
        
        res = self.generate_parenthesis('(', open_count + 1, close_count, n)

        return res
        