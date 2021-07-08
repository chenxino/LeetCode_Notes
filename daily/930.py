from typing import List
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        now_count = 0
        end = 0
        for j in range(len(nums)):
            if sum(nums[0:j+1]) == goal:
                now_count = 1
                h = 1
                end = j
                while j+h < len(nums):

                    if (nums[j+h]) == 0:
                        now_count += 1
                        end = j+h
                        h += 1
                    else:
                        break
                break
        count = now_count
        if count == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i-1] == 1:
                now_count = 0
                for j in range(end+1, len(nums)):
                    if nums[j] == 1:
                        now_count += 1
                        end = j
                        h = 1
                        while j+h < len(nums):
                            if (nums[j+h]) == 0:
                                now_count += 1
                                h += 1
                                end = j+h
                            else:
                                break
                        break
                    if end+1 == len(nums):
                        break
            elif goal == 0:
                now_count -= 1
            count += now_count
        return count

print(Solution().numSubarraysWithSum([0,0,0,0,0], 0))