class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        index = 0
        # while index < len(self.nums) and self.nums[index] < num:
        #     index += 1
        if self.nums == []:
            self.nums.append(num)
            return 
        start = 0
        end = len(self.nums)-1
        while start < end:
            index = int((start+end)/2)
            if self.nums[index] < num:
                start =  index+1
            elif self.nums[index] == num:
                self.nums.insert(index, num)
                return 
            else:
                end = index - 1
        if self.nums[start] < num:
            index = start + 1
        else:
            index = start

        self.nums.insert(index, num)

    def findMedian(self) -> float:
        if self.nums == []:
            return None
        if len(self.nums)%2:
            return self.nums[int(len(self.nums)/2)]
        else:
            # print(len(self.nums))
            # print(self.nums)
            return (self.nums[int(len(self.nums)/2)] + self.nums[int(len(self.nums)/2-1)])/2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()