"""
LeetCode Problem 217: Contains Duplicate
Difficulty: Easy
Topics: Array, Hash Table, Sorting

Problem:
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Approach:
Use a hash set to track seen elements. If we encounter an element already in the set, 
return True. Otherwise, add it to the set and continue.
Time Complexity: O(n) - single pass through the array
Space Complexity: O(n) - hash set storage
"""

from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    """
    Check if the array contains any duplicate elements.
    
    Args:
        nums: List of integers
        
    Returns:
        True if any value appears at least twice, False otherwise
    """
    # Create a set to track seen elements
    seen = set()
    
    # Iterate through the array
    for num in nums:
        # If we've seen this number before, return True
        if num in seen:
            return True
        # Otherwise, add it to the set
        seen.add(num)
    
    # No duplicates found
    return False

# Alternative approach using sorting
def contains_duplicate_sort(nums: List[int]) -> bool:
    """
    Alternative approach using sorting.
    Time Complexity: O(n log n)
    Space Complexity: O(1) or O(log n) for sorting
    """
    # Sort the array
    nums.sort()
    
    # Check adjacent elements for duplicates
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    
    return False

# Alternative approach using set length comparison
def contains_duplicate_set(nums: List[int]) -> bool:
    """
    Alternative approach: compare length of set vs original array.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return len(nums) != len(set(nums))

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 1]
    expected1 = True
    result1 = contains_duplicate(nums1)
    print(f"Test 1:")
    print(f"  Input: {nums1}")
    print(f"  Output: {result1}")
    print(f"  Expected: {expected1}")
    assert result1 == expected1
    
    # Test case 2
    nums2 = [1, 2, 3, 4]
    expected2 = False
    result2 = contains_duplicate(nums2)
    print(f"\nTest 2:")
    print(f"  Input: {nums2}")
    print(f"  Output: {result2}")
    print(f"  Expected: {expected2}")
    assert result2 == expected2
    
    # Test case 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    expected3 = True
    result3 = contains_duplicate(nums3)
    print(f"\nTest 3:")
    print(f"  Input: {nums3}")
    print(f"  Output: {result3}")
    print(f"  Expected: {expected3}")
    assert result3 == expected3
    
    # Test case 4: Empty array (though constraints say min length 1)
    nums4 = []
    expected4 = False
    result4 = contains_duplicate(nums4)
    print(f"\nTest 4:")
    print(f"  Input: {nums4}")
    print(f"  Output: {result4}")
    print(f"  Expected: {expected4}")
    assert result4 == expected4
    
    # Test case 5: Single element
    nums5 = [5]
    expected5 = False
    result5 = contains_duplicate(nums5)
    print(f"\nTest 5:")
    print(f"  Input: {nums5}")
    print(f"  Output: {result5}")
    print(f"  Expected: {expected5}")
    assert result5 == expected5
    
    # Test case 6: Two identical elements
    nums6 = [7, 7]
    expected6 = True
    result6 = contains_duplicate(nums6)
    print(f"\nTest 6:")
    print(f"  Input: {nums6}")
    print(f"  Output: {result6}")
    print(f"  Expected: {expected6}")
    assert result6 == expected6
    
    # Test case 7: Negative numbers
    nums7 = [-1, -2, -3, -1]
    expected7 = True
    result7 = contains_duplicate(nums7)
    print(f"\nTest 7:")
    print(f"  Input: {nums7}")
    print(f"  Output: {result7}")
    print(f"  Expected: {expected7}")
    assert result7 == expected7
    
    # Test case 8: Large array with no duplicates
    nums8 = list(range(1000))
    expected8 = False
    result8 = contains_duplicate(nums8)
    print(f"\nTest 8:")
    print(f"  Input: array of 0-999")
    print(f"  Output: {result8}")
    print(f"  Expected: {expected8}")
    assert result8 == expected8
    
    print("\nAll tests passed!")