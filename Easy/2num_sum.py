def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return sorted([potentialMatch, num])
        else:
            nums[num] = True
    return []