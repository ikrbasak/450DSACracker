#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author = Krishna Basak (https://www.github.com/ikrbasak)
# Date = 04-10-2022

# Find the "Kth" max and min element of an array


def kth_max_n_min_element(arr: list, k: int):
    arr.sort(reverse=True)
    return f"Max = {arr[-k]}, Min = {arr[k - 1]}"


def main():
    t = int(input())
    for i in range(t):
        n, k = list(map(int, input().split(" ")))
        x = list(map(str, input().split(" ")))
        print(kth_max_n_min_element(x, k))


if __name__ == "__main__":
    main()
