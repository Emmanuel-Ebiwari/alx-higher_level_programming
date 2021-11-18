#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    count = 0
    print("{:d} argument{}{}"
          .format(len(argv) - 1, "s" if len(argv) != 2 else "",
                  ":" if len(argv) > 1 else "."))
    while count < len(argv) - 1:
        print("{:d}: {}".format(count + 1, argv[count + 1]))
        count += 1
