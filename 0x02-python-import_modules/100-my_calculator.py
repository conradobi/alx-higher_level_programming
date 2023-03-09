#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    a = int(sys.argv[1])
    op_rat_or = sys.argv[2]
    b = int(sys.argv[3])
    if (len(sys.argv) - 1) != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)

    if op_rat_or == "+":
        print('{} + {} = {}'.format(a, b, calculator_1.add(a,b)))
    elif op_rat_or == "-":
        print('{} - {} = {}'.format(a, b, calculator_1.sub(a,b)))
    elif op_rat_or == "/":
        print('{} / {} = {}'.format(a, b, calculator_1.div(a,b)))
    elif op_rat_or == "*":
        print('{} * {} = {}'.format(a, b, calculator_1.mul(a,b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
