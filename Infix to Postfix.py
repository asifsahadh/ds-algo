def infix_to_postfix(infix):

    pres = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '^' : 3}
    postfix = ''
    stack = []

    for e in infix:
        if e.isalnum():
            postfix += e
        elif e == '(':
            stack.append(e)
        elif e == ')':
            while stack[-1] != '(':
                ele = stack.pop()
                postfix += ele
            stack.pop() # removing ')'
        else:
            while stack and stack[-1] != '(' and pres[stack[-1]] >= pres[e]:
                postfix += stack.pop()
            stack.append(e)
    while stack:
        postfix += stack.pop()
        
    return postfix