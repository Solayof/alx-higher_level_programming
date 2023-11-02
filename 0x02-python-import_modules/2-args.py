#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    in_put = argv[1:]
    lent = len(in_put)
    print("{:d} {:s}{:s}".
          format(lent,
                 "arguments" if (lent) != 1 else "argument",
                 "." if (lent) == 0 else ":"))
    for x, value in enumerate(in_put):
        print("{:d}: {:s}".format(x + 1, value))
