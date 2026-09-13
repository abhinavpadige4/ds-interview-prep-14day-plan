"""
LeetCode Problem 169: Majority Element
Difficulty: Easy
Topics: Array, Hash Table, Divide and Conquer, Sorting, Counting

Problem:
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
- n == nums.length
- 1 <= n <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9

Approach:
Use Boyer-Moore Voting Algorithm:
- Maintain a candidate and count
- When count is 0, set current element as candidate
- If current element equals candidate, increment count
- Otherwise, decrement count
- The candidate at the end is the majority element
Time Complexity: O(n) - single pass through the array
Space Complexity: O(1) - constant space
"""

from typing import List

def majority_element(nums: List[int]) -> int:
    """
    Find the majority element that appears more than ⌊n/2⌋ times.
    
    Args:
        nums: List of integers
        
    Returns:
        The majority element
    """
    # Boyer-Moore Voting Algorithm
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    return candidate

# Alternative approach using hash map
def majority_element_hashmap(nums: List[int]) -> int:
    """
    Alternative approach using hash map to count frequencies.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    from collections import Counter
    
    count = Counter(nums)
    n = len(nums)
    
    for num, freq in count.items():
        if freq > n // 2:
            return num
    
    return -1  # Should never reach here per problem constraints

# Alternative approach using sorting
def majority_element_sort(nums: List[int]) -> int:
    """
    Alternative approach using sorting.
    Time Complexity: O(n log n)
    Space Complexity: O(1) or O(log n) for sorting
    """
    nums.sort()
    return nums[len(nums) // 2]

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [3, 2, 3]
    expected1 = 3
    result1 = majority_element(nums1)
    print(f"Test 1:")
    print(f"  Input: {nums1}")
    print(f"  Output: {result1}")
    print(f"  Expected: {expected1}")
    assert result1 == expected1
    
    # Test case 2
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    expected2 = 2
    result2 = majority_element(nums2)
    print(f"\nTest 2:")
    print(f"  Input: {nums2}")
    print(f"  Output: {result2}")
    print(f"  Expected: {expected2}")
    assert result2 == expected2
    
    # Test case 3: Single element
    nums3 = [5]
    expected3 = 5
    result3 = majority_element(nums3)
    print(f"\nTest 3:")
    print(f"  Input: {nums3}")
    print(f"  Output: {result3}")
    print(f"  Expected: {expected3}")
    assert result3 == expected3
    
    # Test case 4: All same elements
    nums4 = [7, 7, 7, 7, 7]
    expected4 = 7
    result4 = majority_element(nums4)
    print(f"\nTest 4:")
    print(f"  Input: {nums4}")
    print(f"  Output: {result4}")
    print(f"  Expected: {expected4}")
    assert result4 == expected4
    
    # Test case 5: Majority at the beginning
    nums5 = [1, 1, 1, 2, 3, 4, 5]
    expected5 = 1
    result5 = majority_element(nums5)
    print(f"\nTest 5:")
    print(f"  Input: {nums5}")
    print(f"  Output: {result5}")
    print(f"  Expected: {expected5}")
    assert result5 == expected5
    
    # Test case 6: Majority at the end
    nums6 = [1, 2, 3, 4, 5, 5, 5, 5, 5]
    expected6 = 5
    result6 = majority_element(nums6)
    print(f"\nTest 6:")
    print(f"  Input: {nums6}")
    print(f"  Output: {result6}")
    print(f"  Expected: {expected6}")
    assert result6 == expected6
    
    # Test case 7: Large array
    nums7 = [2] * 1000 + [1] * 499  # 2 appears 1000 times, 1 appears 499 times
    expected7 = 2
    result7 = majority_element(nums7)
    print(f"\nTest 7:")
    print(f"  Input: array with 1000 twos and 499 ones")
    print(f"  Output: {result7}")
    print(f"  Expected: {expected7}")
    assert result7 == expected7
    
    print("\nAll tests passed!")