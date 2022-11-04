# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3

def calc(first, operator, second):
    if operator == "*":
        return first * second
    elif operator == "/":
        return first // second
    elif operator == "+":
        return first + second
    else:
        return first - second


def zero(*args): return 0 if not args else calc(0, args[0][0], args[0][1])
def one(*args): return 1 if not args else calc(1, args[0][0], args[0][1])
def two(*args): return 2 if not args else calc(2, args[0][0], args[0][1])
def three(*args): return 3 if not args else calc(3, args[0][0], args[0][1])
def four(*args): return 4 if not args else calc(4, args[0][0], args[0][1])
def five(*args): return 5 if not args else calc(5, args[0][0], args[0][1])
def six(*args): return 6 if not args else calc(6, args[0][0], args[0][1])
def seven(*args): return 7 if not args else calc(7, args[0][0], args[0][1])
def eight(*args): return 8 if not args else calc(8, args[0][0], args[0][1])
def nine(*args): return 9 if not args else calc(9, args[0][0], args[0][1])


def plus(*args): return "+", args[0]
def minus(*args): return "-", args[0]
def times(*args): return "*", args[0]
def divided_by(*args): return "/", args[0]

# test.assert_equals(four(plus(nine())), 13)
# test.assert_equals(eight(minus(three())), 5)
# test.assert_equals(six(divided_by(two())), 3)

print(four(plus(nine())))