def solution(arr1):
    return [arr1[-1]] + arr1[:-1]


if __name__ == "__main__":
    list1 = input().split(" ")
    result = solution(list1)
    print(result)
