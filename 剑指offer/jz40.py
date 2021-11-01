class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def my_find(arr, k):
            if arr == []:
                return []
            small = -1
            for i in range(len(arr) - 1):
                if arr[i] < arr[-1]:
                    small += 1
                    if i != small:
                        arr[i], arr[small] = arr[small], arr[i]
            small += 1
            arr[-1], arr[small] = arr[small], arr[-1]
            print(small)
            print(arr[:small+1])
            if k == small+1:
                return arr[:small+1]
            elif k < small+1:
                return my_find(arr[:small], k)
            else:
                return arr[:small+1] + my_find(arr[small+1:], k-small-1)
        return my_find(arr, k)
