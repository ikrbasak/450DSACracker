#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author = Krishna Basak (https://www.github.com/ikrbasak)
# Date = 04-10-2022

# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo


def main():
    n = int(input())  # noqa
    arr = list(map(int, input().split(" ")))

    n0 = arr.count(0)
    n1 = arr.count(1)
    n2 = arr.count(2)

    result = [0] * n0 + [1] * n1 + [2] * n2
    print(result)


if __name__ == "__main__":
    main()
