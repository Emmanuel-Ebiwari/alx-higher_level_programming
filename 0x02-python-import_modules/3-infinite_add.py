#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv) - 1
    total = 0
    count = 0
    while count < argc:
        total += int(argv[count + 1])
        count += 1
    print(total)
