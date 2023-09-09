class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 0
        temp_1 = 0
        temp_2 = 0
        indice = []
        while i < len(nums):
            temp_1 = nums[i]
            while j + 1 < len(nums):
                temp_2 = nums[j + 1]
                if((temp_1 + temp_2) == target):
                    indice.append(i)
                    indice.append(j+1)
                    return indice
                j = j + 1
            i = i + 1
            j = i
