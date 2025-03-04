from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        j = 0  # Con trỏ để ghi lại vị trí cần ghi đè phần tử không trùng
        
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:  # Nếu gặp phần tử khác với nums[j]
                j += 1
                nums[j] = nums[i]  # Ghi đè phần tử mới vào vị trí mới
                
        return j + 1  # Số phần tử unique
