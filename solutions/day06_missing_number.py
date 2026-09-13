"""
LeetCode Problem 268: Missing Number
Difficulty: Easy
Topics: Array, Hash Table, Math, Bit Manipulation, Sorting

Problem:
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
8 is the missing number in the range since it does not appear in nums.

Constraints:
- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All the numbers of nums are unique.

Approach:
Use mathematical formula: sum of first n natural numbers = n*(n+1)/2
Missing number = expected_sum - actual_sum
Time Complexity: O(n) - single pass to calculate sum
Space Complexity: O(1) - constant space
"""

from typing import List

def missing_number(nums: List[int]) -> int:
    """
    Find the missing number in an array containing n distinct numbers in range [0, n].
    
    Args:
        nums: List of integers containing n distinct numbers from 0 to n (missing one)
        
    Returns:
        The missing number in the range [0, n]
    """
    n = len(nums)
    
    # Calculate expected sum of numbers from 0 to n
    # Formula: n*(n+1)/2
    expected_sum = n * (n + 1) // 2
    
    # Calculate actual sum of array elements
    actual_sum = sum(nums)
    
    # The difference is the missing number
    return expected_sum - actual_sum

# Alternative approach using XOR
def missing_number_xor(nums: List[int]) -> int:
    """
    Alternative approach using XOR operation.
    Property: a XOR a = 0, a XOR 0 = a
    XOR all indices and values, the missing number will remain.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    missing = len(nums)
    
    for i, num in enumerate(nums):
        missing ^= i ^ num
    
    return missing

# Alternative approach using hash set
def missing_number_hashset(nums: List[int]) -> int:
    """
    Alternative approach using hash set.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    num_set = set(nums)
    
    for i in range(len(nums) + 1):
        if i not in num_set:
            return i
    
    return -1  # Should never reach here

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [3, 0, 1]
    expected1 = 2
    result1 = missing_number(nums1)
    print(f"Test 1:")
    print(f"  Input: {nums1}")
    print(f"  Output: {result1}")
    print(f"  Expected: {expected1}")
    assert result1 == expected1
    
    # Test case 2
    nums2 = [0, 1]
    expected2 = 2
    result2 = missing_number(nums2)
    print(f"\nTest 2:")
    print(f"  Input: {nums2}")
    print(f"  Output: {result2}")
    print(f"  Expected: {expected2}")
    assert result2 == expected2
    
    # Test case 3
    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    expected3 = 8
    result3 = missing_number(nums3)
    print(f"\nTest 3:")
    print(f"  Input: {nums3}")
    print(f"  Output: {result3}")
    print(f"  Expected: {expected3}")
    assert result3 == expected3
    
    # Test case 4: Missing zero
    nums4 = [1, 2, 3]
    expected4 = 0
    result4 = missing_number(nums4)
    print(f"\nTest 4:")
    print(f"  Input: {nums4}")
    print(f"  Output: {result4}")
    print(f"  Expected: {expected4}")
    assert result4 == expected4
    
    
    # Test case 5: Missing last number
    nums5 = [0, 1, 2, 3]
    expected5 = 4
    result5 = missing_number(nums5)
    print(f"\nTest 5:")
    print(f"  Input: {nums5}")
    print(f"  Output: {result5}")
    print(f"  Expected: {expected5}")
    assert result5 == expected5
    
    # Test case 6: Single element array (missing 1)
    nums6 = [0]
    expected6 = 1
    result6 = missing_number(nums6)
    print(f"\nTest 6:")
    print(f"  Input: {nums6}")
    print(f"  Output: {result6}")
    print(f"  Expected: {expected6}")
    assert result6 == expected6
    
    # Test case 7: Single element array (missing 0)
    nums7 = [1]
    expected7 = 0
    result7 = missing_number(nums7)
    print(f"\nTest 7:")
    print(f"  Input: {nums7}")
    print(f"  Output: {result7}")
    print(f"  Expected: {expected7}")
    assert result7 == expected7
    
    print("\nAll tests passed!")