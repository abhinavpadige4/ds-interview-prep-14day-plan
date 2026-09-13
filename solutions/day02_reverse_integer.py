"""
LeetCode Problem 7: Reverse Integer
Difficulty: Easy
Topics: Math

Problem:
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:
-2^31 <= x <= 2^31 - 1

Approach:
Handle the sign separately, then reverse the digits mathematically.
Check for overflow before returning the result.
Time Complexity: O(log(x)) - number of digits in x
Space Complexity: O(1) - constant space
"""

def reverse(x: int) -> int:
    """
    Reverse the digits of a signed 32-bit integer.
    
    Args:
        x: Integer to reverse
        
    Returns:
        Reversed integer, or 0 if reversal causes overflow
    """
    # Define 32-bit integer boundaries
    INT_MAX = 2**31 - 1  # 2147483647
    INT_MIN = -2**31     # -2147483648
    
    # Store the sign and work with positive number
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    
    # Reverse the digits
    reversed_num = 0
    while x_abs > 0:
        # Pop the last digit
        digit = x_abs % 10
        x_abs //= 10
        
        # Check for overflow before pushing the digit
        if reversed_num > (INT_MAX - digit) // 10:
            return 0
            
        # Push the digit
        reversed_num = reversed_num * 10 + digit
    
    # Apply the original sign
    result = sign * reversed_num
    
    # Final overflow check (though intermediate checks should catch this)
    if result < INT_MIN or result > INT_MAX:
        return 0
        
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    x1 = 123
    result1 = reverse(x1)
    print(f"Test 1: x = {x1}")
    print(f"Result: {result1}")  # Expected: 321
    assert result1 == 321
    
    # Test case 2
    x2 = -123
    result2 = reverse(x2)
    print(f"\nTest 2: x = {x2}")
    print(f"Result: {result2}")  # Expected: -321
    assert result2 == -321
    
    # Test case 3
    x3 = 120
    result3 = reverse(x3)
    print(f"\nTest 3: x = {x3}")
    print(f"Result: {result3}")  # Expected: 21
    assert result3 == 21
    
    # Test case 4: Overflow case
    x4 = 1534236469
    result4 = reverse(x4)
    print(f"\nTest 4: x = {x4} (overflow case)")
    print(f"Result: {result4}")  # Expected: 0
    assert result4 == 0
    
    # Test case 5: Negative overflow case
    x5 = -2147483412
    result5 = reverse(x5)
    print(f"\nTest 5: x = {x5} (negative overflow case)")
    print(f"Result: {result5}")  # Expected: 0
    assert result5 == 0
    
    print("\nAll tests passed!")