from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        r, l = n-1, 0
        while r>=l:
            mid = int((r+l)/2)
            if nums[mid] > target:
                r = mid-1
            elif nums[mid]< target:
                l = mid+1
            elif nums[mid] == target:
                break
        if r<l: 
            return 0
        i,j = mid-1, mid+1
        count = 1
        while i<n and i>=0 and nums[i] ==target:
            count+=1
            i-=1
        while j<n and j>=0 and nums[j]==target:
            count+=1
            j+=1
        return count


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        r, l = n-1, 0
        while r>=l:
            mid = int((r+l)/2)
            if nums[mid] >= target:
                r = mid-1
            elif nums[mid]< target:
                l = mid+1
        i = r
        if l <= n-1 and nums[l] != target: return 0
        r, l = n-1, i
        while r>=l:
            mid = int((r+l)/2)
            if nums[mid] > target:
                r = mid-1
            elif nums[mid]<= target:
                l = mid+1
        j = l
        
        return j - i - 1

result = Solution().search([2,2],
3)
print(result)