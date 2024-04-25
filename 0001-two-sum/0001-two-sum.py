class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        di={}
        for i in range(n):
            if target-nums[i] in di.keys():
                return[di[target-nums[i]],i]
            di[nums[i]]=i
        print(di)