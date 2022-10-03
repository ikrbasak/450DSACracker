#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author = Krishna Basak (https://www.github.com/ikrbasak)
# Date = 03-10-2022

# Find the maximum and minimum element in an array


def max_n_min_element(arr):
    mx = max(arr)
    mn = min(arr)
    return f"Max = {mx}, Min = {mn}"


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        x = list(map(str, input().split(" ")))

        print(max_n_min_element(x))


if __name__ == "__main__":
    main()
