"""
LeetCode Problem 283: Move Zeroes
Difficulty: Easy
Topics: Array, Two Pointers

Problem:
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

Approach:
Use two pointers technique:
- Slow pointer tracks the position to place next non-zero element
- Fast pointer scans through the array
When fast pointer finds a non-zero element, swap it with slow pointer position
Time Complexity: O(n) - single pass through the array
Space Complexity: O(1) - in-place modification
"""

from typing import List

def move_zeroes(nums: List[int]) -> None:
    """
    Move all zeroes to the end of the array while maintaining relative order of non-zero elements.
    
    Args:
        nums: List of integers to be modified in-place
        
    Returns:
        None (modifies nums in-place)
    """
    # Two pointers approach
    # slow pointer tracks position to place next non-zero element
    slow = 0
    
    # fast pointer scans through the array
    for fast in range(len(nums)):
        # When we find a non-zero element
        if nums[fast] != 0:
            # Swap elements at slow and fast pointers
            nums[slow], nums[fast] = nums[fast], nums[slow]
            # Move slow pointer forward
            slow += 1

# Alternative approach: copy non-zeros first, then fill zeros
def move_zeroes_copy_then_fill(nums: List[int]) -> None:
    """
    Alternative approach: copy all non-zero elements first, then fill remaining with zeros.
    """
    # Index to place next non-zero element
    insert_pos = 0
    
    # Copy all non-zero elements to the front
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    
    # Fill remaining positions with zeros
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [0, 1, 0, 3, 12]
    expected1 = [1, 3, 12, 0, 0]
    move_zeroes(nums1)
    print(f"Test 1:")
    print(f"  Input: [0, 1, 0, 3, 12]")
    print(f"  Output: {nums1}")
    print(f"  Expected: {expected1}")
    assert nums1 == expected1
    
    # Test case 2
    nums2 = [0]
    expected2 = [0]
    move_zeroes(nums2)
    print(f"\nTest 2:")
    print(f"  Input: [0]")
    print(f"  Output: {nums2}")
    print(f"  Expected: {expected2}")
    assert nums2 == expected2
    
    # Test case 3: No zeros
    nums3 = [1, 2, 3, 4, 5]
    expected3 = [1, 2, 3, 4, 5]
    move_zeroes(nums3)
    print(f"\nTest 3:")
    print(f"  Input: [1, 2, 3, 4, 5]")
    print(f"  Output: {nums3}")
    print(f"  Expected: {expected3}")
    assert nums3 == expected3
    
    # Test case 4: All zeros
    nums4 = [0, 0, 0, 0]
    expected4 = [0, 0, 0, 0]
    move_zeroes(nums4)
    print(f"\nTest 4:")
    print(f"  Input: [0, 0, 0, 0]")
    print(f"  Output: {nums4}")
    print(f"  Expected: {expected4}")
    assert nums4 == expected4
    
    # Test case 5: Zeros at the end already
    nums5 = [1, 2, 3, 0, 0]
    expected5 = [1, 2, 3, 0, 0]
    move_zeroes(nums5)
    print(f"\nTest 5:")
    print(f"  Input: [1, 2, 3, 0, 0]")
    print(f"  Output: {nums5}")
    print(f"  Expected: {expected5}")
    assert nums5 == expected5
    
    # Test case 6: Single non-zero
    nums6 = [5]
    expected6 = [5]
    move_zeroes(nums6)
    print(f"\nTest 6:")
    print(f"  Input: [5]")
    print(f"  Output: {nums6}")
    print(f"  Expected: {expected6}")
    assert nums6 == expected6
    
    print("\nAll tests passed!")