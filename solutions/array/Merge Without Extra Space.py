def solution(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    return sorted(arr1 + arr2)[:m], sorted(arr1 + arr2)[m : (m + n)]


if __name__ == "__main__":
    list1 = input().split(" ")
    list2 = input().split(" ")
    list1, list2 = solution(list1, list2)
    print(list1, list2)
