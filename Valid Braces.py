# s = "(){}[]"
# s = "([{}])"
# s = "(}"
# s = "[(])"
# s = "[({})](]"
# s = "(({{[[]]}}))"
s = "())({}}{()][]["

#
# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False


def valid_braces(string):
    stack = []
    try:
        for char in string:
            if char in "([{":
                stack.append(char)
            elif char == ")" and stack[len(stack) - 1] == "(":
                stack.pop(len(stack) - 1)
            elif char == "}" and stack[len(stack) - 1] == "{":
                stack.pop(len(stack) - 1)
            elif char == "]" and stack[len(stack) - 1] == "[":
                stack.pop(len(stack) - 1)
    except IndexError:
        return False
    return True if len(stack) == 0 else False

print(valid_braces(s))