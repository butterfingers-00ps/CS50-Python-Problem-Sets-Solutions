import operator


def main():
    expression = input("Expression: ")
    x, y, z = expression.split()

    x = float(x)
    z = float(z)

    operation = get_operation(y)
    ans = operation(x, z)

    print(round(ans, 1))

def get_operation(y):

    if y == "+":
        return operator.add
    elif y == "-":
         return operator.sub
    elif y == "*":
          return operator.mul
    elif y == "/":
          return operator.truediv

main()
