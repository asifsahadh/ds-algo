def postfix_eval(postfix):
    
    stack = []
    for e in postfix:
        if e.isalnum():
            stack.append(int(e))
        else:
            b = stack.pop()
            a = stack.pop()
            if e == '+':
                stack.append(a + b)
            elif e == '-':
                stack.append(a - b)
            elif e == '*':
                stack.append(a * b)
            elif e == '/':
                stack.append(a / b)
            elif e == '^':
                stack.append(a ** b)
    return stack[-1]