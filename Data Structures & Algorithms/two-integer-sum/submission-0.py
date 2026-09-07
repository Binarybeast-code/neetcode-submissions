class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_dict = {}

        for i in range(len(nums)): #iterating the list
            if  target - nums[i] in num_dict: #check if the number is already on the list
                return [num_dict[target - nums[i]], i] #return result if found
            num_dict[nums[i]] = i  #not found add it to the dictionary
        
        return []