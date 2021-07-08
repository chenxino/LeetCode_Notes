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
        print(now_count)
        if count == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i-1] == 1:
                if goal == 0:
                    for j in range(end+1, len(nums)):
                        if sum(nums[i:j+1]) == goal:
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
                else:
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
            if end < i:
                end  = i
            print(now_count)
            count += now_count
        return count

print(Solution().numSubarraysWithSum([1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0], 0))