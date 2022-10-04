#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author = Krishna Basak (https://www.github.com/ikrbasak)
# Date = 04-10-2022

# Move all the negative elements to one side of the array


def main():
    n = int(input())  # noqa
    arr = list(map(int, input().split(" ")))
    arr.sort()
    print(arr)


if __name__ == "__main__":
    main()
