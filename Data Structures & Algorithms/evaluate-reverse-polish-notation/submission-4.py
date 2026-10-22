class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in range(len(tokens)):
            if tokens[i].isnumeric():
                stack.append(tokens[i])
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                if tokens[i] == "+":
                    new = second + first
                    stack.append(new)
                elif tokens[i] == "-":
                    new = first - second
                    stack.append(new)
                elif tokens[i] == "*":
                    new = second * first
                    stack.append(new)
                elif tokens[i] == "/":
                    new = first / second
                    stack.append(new)
            
        
        last = stack.pop()
        return last