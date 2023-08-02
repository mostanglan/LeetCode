def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    result = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            sumArr = nums[i] + nums[l] + nums[r]
            if sumArr < 0:
                l+=1
            elif sumArr > 0:
                r-=1
            else:
                result.append([nums[i],nums[l],nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l+=1
                while l < r and nums[r] == nums[r-1]:
                    r-=1
                l+=1
                r-=1
            
    return result

print(threeSum([-1, 0, 1, 2, -1, -4]))
