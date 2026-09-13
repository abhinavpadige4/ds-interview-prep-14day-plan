"""
LeetCode Problem 136: Single Number
Difficulty: Easy
Topics: Array, Bit Manipulation

Problem:
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output:1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
- Each element in the array appears twice except for one element which appears only once.

Approach:
Use XOR operation properties:
- a XOR a = 0
- a XOR 0 = a
- XOR is commutative and associative
- XOR all elements: pairs cancel out (become 0), leaving only the single number
Time Complexity: O(n) - single pass through the array
Space Complexity: O(1) - constant space
"""

from typing import List

def single_number(nums: List[int]) -> int:
    """
    Find the element that appears only once in an array where every other element appears twice.
    
    Args:
        nums: List of integers where every element appears twice except one
        
    Returns:
        The single element that appears only once
    """
    # Initialize result to 0
    result = 0
    
    # XOR all elements together
    # Pairs will cancel out: a XOR a = 0
    # The single number will remain: 0 XOR a = a
    for num in nums:
        result ^= num
    
    return result

# Alternative approach using hash map (for educational purposes)
def single_number_hashmap(nums: List[int]) -> int:
    """
    Alternative approach using hash map to count frequencies.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    from collections import Counter
    
    freq_map = Counter(nums)
    
    for num, count in freq_map.items():
        if count == 1:
            return num
    
    return -1  # Should never reach here per problem constraints

# Alternative approach using mathematical set
def single_number_math(nums: List[int]) -> int:
    """
    Alternative approach using mathematical property:
    2 * sum(set(nums)) - sum(nums) = single number
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return 2 * sum(set(nums)) - sum(nums)

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 2, 1]
    expected1 = 1
    result1 = single_number(nums1)
    print(f"Test 1:")
    print(f"  Input: {nums1}")
    print(f"  Output: {result1}")
    print(f"  Expected: {expected1}")
    assert result1 == expected1
    
    # Test case 2
    nums2 = [4, 1, 2, 1, 2]
    expected2 = 4
    result2 = single_number(nums2)
    print(f"\nTest 2:")
    print(f"  Input: {nums2}")
    print(f"  Output: {result2}")
    print(f"  Expected: {expected2}")
    assert result2 == expected2
    
    # Test case 3
    nums3 = [1]
    expected3 = 1
    result3 = single_number(nums3)
    print(f"\nTest 3:")
    print(f"  Input: {nums3}")
    print(f"  Output: {result3}")
    print(f"  Expected: {expected3}")
    assert result3 == expected3
    
    # Test case 4: Single number at the beginning
    nums4 = [5, 4, 4, 3, 3]
    expected4 = 5
    result4 = single_number(nums4)
    print(f"\nTest 4:")
    print(f"  Input: {nums4}")
    print(f"  Output: {result4}")
    print(f"  Expected: {expected4}")
    assert result4 == expected4
    
    # Test case 5: Single number at the end
    nums5 = [4, 4, 3, 3, 5]
    expected5 = 5
    result5 = single_number(nums5)
    print(f"\nTest 5:")
    print(f"  Input: {nums5}")
    print(f"  Output: {result5}")
    print(f"  Expected: {expected5}")
    assert result5 == expected5
    
    # Test case 6: Negative numbers
    nums6 = [-1, -1, -2]
    expected6 = -2
    result6 = single_number(nums6)
    print(f"\nTest 6:")
    print(f"  Input: {nums6}")
    print(f"  Output: {result6}")
    print(f"  Expected: {expected6}")
    assert result6 == expected6
    
    # Test case 7: Larger array
    nums7 = [1, 1, 2, 2, 3, 4, 4, 5, 5]
    expected7 = 3
    result7 = single_number(nums7)
    print(f"\nTest 7:")
    print(f"  Input: {nums7}")
    print(f"  Output: {result7}")
    print(f"  Expected: {expected7}")
    assert result7 == expected7
    
    # Test case 8: All same except one
    nums8 = [7, 7, 7, 7, 8, 7, 7]
    expected8 = 8
    result8 = single_number(nums8)
    print(f"\nTest 8:")
    print(f"  Input: {nums8}")
    print(f"  Output: {result8}")
    print(f"  Expected: {expected8}")
    assert result8 == expected8
    
    # Verify with alternative methods
    print(f"\nVerifying with alternative methods:")
    test_cases = [
        [2, 2, 1],
        [4, 1, 2, 1, 2],
        [1],
        [5, 4, 4, 3, 3],
        [-1, -1, -2],
        [1, 1, 2, 2, 3, 4, 4, 5, 5]
    ]
    
    for nums in test_cases:
        result1 = single_number(nums)
        result2 = single_number_hashmap(nums)
        result3 = single_number_math(nums)
        print(f"  {nums}: XOR={result1}, HashMap={result2}, Math={result3} - {'✓' if result1 == result2 == result3 else '✗'}")
        assert result1 == result2 == result3
    
    print("\nAll tests passed!")