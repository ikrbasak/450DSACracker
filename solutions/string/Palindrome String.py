def is_palindrome(s):
    q = ""
    for i in range(len(s) - 1, -1, -1):
        q += s[i]
    print(s, q)
    return s == q


if __name__ == "__main__":
    string = input()
    result = is_palindrome(string)
    print(result)
