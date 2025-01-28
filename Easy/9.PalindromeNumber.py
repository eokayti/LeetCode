class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Nếu x là số âm, chắc chắn không phải là số đối xứng
        if x < 0:
            return False
        
        # Chuyển số thành chuỗi
        x_str = str(x)
        
        # So sánh chuỗi ban đầu với chuỗi đảo ngược
        return x_str == x_str[::-1]
