def main(t):
    q = ""
    for i in range(len(t) - 1, -1, -1):
        q += t[i]
    return q


if __name__ == "__main__":
    s = input()
    r = main(s)
    print(r)
