from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Cách 1: Sử dụng vòng lặp lồng nhau
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # Bắt đầu từ i+1
                if nums[i] + nums[j] == target:
                    return [i, j]  # Trả về chỉ số của 2 phần tử
        
        # Nếu không tìm thấy kết quả (không có cặp thỏa mãn)
        return []