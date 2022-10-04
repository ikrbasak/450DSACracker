#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author = Krishna Basak (https://www.github.com/ikrbasak)
# Date = 04-10-2022

# Count set bits in an integer


def main():
    n = int(input())
    n = [a for a in str(bin(n))[2:]]
    print(n.count("1"))


if __name__ == "__main__":
    main()
