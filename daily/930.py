from typing import List
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0

        if goal == 0:
            cc = 0
            for i in range(len(nums)):
                if nums[i] == 0:
                    cc += 1
                else:
                    for c in range(cc):
                        count += c+1
                    cc = 0
            for c in range(cc):
                count += c+1
            return count
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
                now_count = 0
                for j in range(end+1, len(nums)):
                    if nums[j] == 1:
                        now_count += 1
                        end = j
                        h = 1
                        while j+h < len(nums):
                            if (nums[j+h]) == 0:
                                now_count += 1
                                end = j+h
                                h += 1
                            else:
                                break
                        break
                    if end+1 == len(nums):
                        break
            print(now_count)
            count += now_count
        return count

print(Solution().numSubarraysWithSum([0,0,0,1,0,1,0,1,1,1,0,0,1,0,1,1,0,1,1,0], 3))


# 大佬解法 作者：AC_OIer
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        presum = [0] + list(accumulate(nums))
        hashmap = defaultdict(int, {0:1})
        ans = 0
        for i in range(n):
            r = presum[i+1]
            l = r - goal
            ans += hashmap[l]
            hashmap[r] += 1
        return ans
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        ans = l1 = l2 = s1 = s2 = 0
        for r in range(n):
            s1 += nums[r]
            s2 += nums[r]
            while l1 <= r and s1 > goal:
                s1 -= nums[l1]
                l1 += 1
            while l2 <= r and s2 >= goal:
                s2 -= nums[l2]
                l2 += 1
            ans += l2 - l1
        return ans

