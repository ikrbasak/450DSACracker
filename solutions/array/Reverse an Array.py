#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author = Krishna Basak (https://www.github.com/ikrbasak)
# Date = 03-10-2022

# Reverse an Array


def reverse(arr, l):
    return [arr[i] for i in range(l - 1, -1, -1)]


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        x = list(map(str, input().split(" ")))

        print(" ".join(reverse(x, n)))


if __name__ == "__main__":
    main()
