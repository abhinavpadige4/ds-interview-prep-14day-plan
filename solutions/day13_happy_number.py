"""
LeetCode Problem 202: Happy Number
Difficulty: Easy
Topics: Hash Table, Math, Two Pointers

Problem:
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle 
  which does not include 1.
- Those numbers for which this process ends in 1 are happy.
- Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 2
Output: false

Constraints:
- 1 <= n <= 2^31 - 1

Approach:
Use hash set to detect cycles. If we see a number again, we're in a loop.
Alternatively, use Floyd's Cycle Finding Algorithm (tortoise and hare).
Time Complexity: O(log n) per iteration, but number of iterations is bounded
Space Complexity: O(log n) for hash set approach, O(1) for two pointers
"""

def is_happy(n: int) -> bool:
    """
    Determine if a number is happy using hash set to detect cycles.
    
    Args:
        n: Positive integer to check
        
    Returns:
        True if n is a happy number, False otherwise
    """
    def get_next(number):
        """Calculate sum of squares of digits"""
        total_sum = 0
        while number > 0:
            digit = number % 10
            total_sum += digit * digit
            number //= 10
        return total_sum
    
    # Use set to detect cycles
    seen = set()
    
    # Continue until we reach 1 (happy) or detect a cycle
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    
    return n == 1

# Alternative approach using Floyd's Cycle Finding Algorithm (Tortoise and Hare)
def is_happy_floyd(n: int) -> bool:
    """
    Determine if a number is happy using Floyd's Cycle Finding Algorithm.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    def get_next(number):
        """Calculate sum of squares of digits"""
        total_sum = 0
        while number > 0:
            digit = number % 10
            total_sum += digit * digit
            number //= 10
        return total_sum
    
    # Initialize slow and fast pointers
    slow = n
    fast = get_next(n)
    
    # Move slow by 1 step, fast by 2 steps until they meet or fast reaches 1
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    
    return fast == 1

# Test cases
if __name__ == "__main__":
    # Test case 1
    n1 = 19
    expected1 = True
    result1 = is_happy(n1)
    print(f"Test 1:")
    print(f"  Input: n = {n1}")
    print(f"  Output: {result1}")
    print(f"  Expected: {expected1}")
    assert result1 == expected1
    
    # Test case 2
    n2 = 2
    expected2 = False
    result2 = is_happy(n2)
    print(f"\nTest 2:")
    print(f"  Input: n = {n2}")
    print(f"  Output: {result2}")
    print(f"  Expected: {expected2}")
    assert result2 == expected2
    
    # Test case 3: 1 is happy by definition
    n3 = 1
    expected3 = True
    result3 = is_happy(n3)
    print(f"\nTest 3:")
    print(f"  Input: n = {n3}")
    print(f"  Output: {result3}")
    print(f"  Expected: {expected3}")
    assert result3 == expected3
    
    # Test case 4: Another happy number
    n4 = 7
    expected4 = True
    result4 = is_happy(n4)
    print(f"\nTest 4:")
    print(f"  Input: n = {n4}")
    print(f"  Output: {result4}")
    print(f"  Expected: {expected4}")
    assert result4 == expected4
    
    # Test case 5: Unhappy number
    n5 = 4
    expected5 = False
    result5 = is_happy(n5)
    print(f"\nTest 5:")
    print(f"  Input: n = {n5}")
    print(f"  Output: {result5}")
    print(f"  Expected: {expected5}")
    assert result5 == expected5
    
    # Test case 6: Larger happy number
    n6 = 100
    expected6 = True  # 1^2 + 0^2 + 0^2 = 1
    result6 = is_happy(n6)
    print(f"\nTest 6:")
    print(f"  Input: n = {n6}")
    print(f"  Output: {result6}")
    print(f"  Expected: {expected6}")
    assert result6 == expected6
    
    # Test case 7: Another unhappy number
    n7 = 12
    expected7 = False
    result7 = is_happy(n7)
    print(f"\nTest 7:")
    print(f"  Input: n = {n7}")
    print(f"  Output: {result7}")
    print(f"  Expected: {expected7}")
    assert result7 == expected7
    
    # Verify with Floyd's algorithm as well
    print(f"\nVerifying with Floyd's algorithm:")
    for n in [19, 2, 1, 7, 4, 100, 12]:
        result1 = is_happy(n)
        result2 = is_happy_floyd(n)
        print(f"  n={n}: HashSet={result1}, Floyd={result2} - {'✓' if result1 == result2 else '✗'}")
        assert result1 == result2
    
    print("\nAll tests passed!")