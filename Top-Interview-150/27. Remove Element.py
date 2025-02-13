from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Biến đếm số phần tử khác val
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Di chuyển phần tử hợp lệ lên đầu mảng
                k += 1  # Tăng biến đếm
        
        return k
