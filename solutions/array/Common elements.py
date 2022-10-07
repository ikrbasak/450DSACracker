def solution(arr1, arr2, arr3):
    return list(set(arr3).intersection(set(arr1).intersection(set(arr2))))


if __name__ == "__main__":
    list1 = input().split(" ")
    list2 = input().split(" ")
    list3 = input().split(" ")
    result = solution(list1, list2, list3)
    print(result)
