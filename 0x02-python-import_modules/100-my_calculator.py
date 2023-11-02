#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)
    op = argv[2]
    sign = {"+": add, "-": sub, "*": mul, "/": div}
    if op not in sign:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    x = int(argv[1])
    y = int(argv[3])
    print("{:d} {:s} {:d} = {:d}".format(x, op, y, f[op](x, y)))
