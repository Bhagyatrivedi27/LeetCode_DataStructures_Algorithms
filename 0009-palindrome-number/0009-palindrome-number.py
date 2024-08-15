class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        number = x
        reversedNumber = 0
        
        while number > 0:
            digit = number%10
            reversedNumber = reversedNumber * 10 + digit
            number = number//10
        
        return x == reversedNumber
            
        
        