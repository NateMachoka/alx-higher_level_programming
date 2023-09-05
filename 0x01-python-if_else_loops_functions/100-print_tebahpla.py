#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if i % 2 == 1:
        print(f"{chr(i - 32)}", end='')
    else:
        print(f"{chr(i)}", end='')
