class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        for i in range(len(nums)):
            for k in range(len(nums)):
                if nums[i] + nums[k] == target and i < k:
                    l.append(i)
                    l.append(k)
        return l