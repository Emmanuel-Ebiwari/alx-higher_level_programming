#!/usr/bin/python3

for no in range(10):
    for no2 in range(no+1, 10):
        if no2 > 1:
            print(", ", end="")
        print("{:d}{:d}".format(no, no2), end="")
print("\n")
