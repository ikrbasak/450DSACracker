def solution(arr1, arr2):
    union = list(set(arr1).union(set(arr2)))
    intersection = list(set(arr1).intersection(set(arr2)))

    return f"Union = {union}, Intersection = {intersection}"


if __name__ == "__main__":
    list1 = input().split(" ")
    list2 = input().split(" ")
    sol = solution(list1, list2)
    print(sol)
