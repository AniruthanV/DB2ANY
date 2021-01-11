def prefixToPostfixRecursive(expression):
    operators = set(['+', '-', '*', '/'])
    # Pass index by reference by using a list
    # This is the python workaround of passing int by reference
    def helper(expr, index):
        if index[0] == len(expr):
            return

        curr_char = expr[index[0]]
        # If expression is operand, return it
        if curr_char not in operators:
            return curr_char
        else:
            index[0] += 1
            left = helper(expr, index)
            index[0] += 1
            right = helper(expr, index)
            # Append it as operand + operand + operator
            return left + right + curr_char

print(prefixToPostfixRecursive("+A*B/CD"))