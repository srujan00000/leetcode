class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff=float('inf')
        nums.sort()
        for i in range(len(nums)-1):
            l,r=i+1,len(nums)-1
            while l<r:
                threesum=nums[i]+nums[l]+nums[r]
                if threesum==target:
                    return target
                elif abs(target-threesum)<diff:
                    diff=abs(target-threesum)
                    ans=threesum
                if threesum>target:
                    r-=1
                else:
                    l+=1
        return ans