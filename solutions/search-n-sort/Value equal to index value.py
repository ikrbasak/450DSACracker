class Solution:
    @staticmethod
    def value_equal_to_index(list1):
        # code here
        r = []
        for i, j in enumerate(list1):
            if i + 1 == j:
                r.append(j)
        return r


if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.value_equal_to_index(arr)
        if len(ans) == 0:
            print("Not Found")
        else:
            for x in ans:
                print(x, end=" ")
            print()
        tc -= 1
