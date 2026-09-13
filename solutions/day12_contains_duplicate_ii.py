"""
LeetCode Problem 219: Contains Duplicate II
Difficulty: Easy
Topics: Array, Hash Table, Sliding Window

Problem:
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array 
such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 10^5

Approach:
Use sliding window with hash set to maintain elements within window of size k.
As we iterate through the window slides, check if current element exists in the set.
Time Complexity: O(n) - single pass through the array
Space Complexity: O(min(n, k)) - size of the sliding window
"""

from typing import List

def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    """
    Check if there are two distinct indices i and j such that:
    nums[i] == nums[j] and abs(i - j) <= k
    
    Args:
        nums: List of integers
        k: Maximum allowed index difference
        
    Returns:
        True if such pair exists, False otherwise
    """
    # Hash set to maintain sliding window of size k
    window = set()
    
    for i, num in enumerate(nums):
        # If current number is already in window, we found a duplicate within k distance
        if num in window:
            return True
        
        # Add current number to window
        window.add(num)
        
        # Maintain window size of at most k
        # Remove element that is k+1 positions behind current index
        if i >= k:
            window.remove(nums[i - k])
    
    return False

# Alternative approach using hash map to store last seen index
def contains_nearby_duplicate_hashmap(nums: List[int], k: int) -> bool:
    """
    Alternative approach: store last seen index of each element.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Dictionary to store the last seen index of each number
    index_map = {}
    
    for i, num in enumerate(nums):
        # If we've seen this number before and the distance is <= k
        if num in index_map and i - index_map[num] <= k:
            return True
        
        # Update the last seen index
        index_map[num] = i
    
    return False

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 1]
    k1 = 3
    expected1 = True
    result1 = contains_nearby_duplicate(nums1, k1)
    print(f"Test 1:")
    print(f"  Input: nums={nums1}, k={k1}")
    print(f"  Output: {result1}")
    print(f"  Expected: {expected1}")
    assert result1 == expected1
    
    # Test case 2
    nums2 = [1, 0, 1, 1]
    k2 = 1
    expected2 = True
    result2 = contains_nearby_duplicate(nums2, k2)
    print(f"\nTest 2:")
    print(f"  Input: nums={nums2}, k={k2}")
    print(f"  Output: {result2}")
    print(f"  Expected: {expected2}")
    assert result2 == expected2
    
    # Test case 3
    nums3 = [1, 2, 3, 1, 2, 3]
    k3 = 2
    expected3 = False
    result3 = contains_nearby_duplicate(nums3, k3)
    print(f"\nTest 3:")
    print(f"  Input: nums={nums3}, k={k3}")
    print(f"  Output: {result3}")
    print(f"  Expected: {expected3}")
    assert result3 == expected3
    
    # Test case 4: k = 0 (no duplicates allowed at same index)
    nums4 = [1, 2, 3, 1]
    k4 = 0
    expected4 = False
    result4 = contains_nearby_duplicate(nums4, k4)
    print(f"\nTest 4:")
    print(f"  Input: nums={nums4}, k={k4}")
    print(f"  Output: {result4}")
    print(f"  Expected: {expected4}")
    assert result4 == expected4
    
    # Test case 5: Large k (entire array)
    nums5 = [1, 2, 3, 1]
    k5 = 10  # Larger than array length
    expected5 = True
    result5 = contains_nearby_duplicate(nums5, k5)
    print(f"\nTest 5:")
    print(f"  Input: nums={nums5}, k={k5}")
    print(f"  Output: {result5}")
    print(f"  Expected: {expected5}")
    assert result5 == expected5
    
    # Test case 6: No duplicates
    nums6 = [1, 2, 3, 4, 5]
    k6 = 2
    expected6 = False
    result6 = contains_nearby_duplicate(nums6, k6)
    print(f"\nTest 6:")
    print(f"  Input: nums={nums6}, k={k6}")
    print(f"  Output: {result6}")
    print(f"  Expected: {expected6}")
    assert result6 == expected6
    
    # Test case 7: Adjacent duplicates
    nums7 = [1, 1]
    k7 = 1
    expected7 = True
    result7 = contains_nearby_duplicate(nums7, k7)
    print(f"\nTest 7:")
    print(f"  Input: nums={nums7}, k={k7}")
    print(f"  Output: {result7}")
    print(f"  Expected: {expected7}")
    assert result7 == expected7
    
    # Test case 8: Duplicates just outside window
    nums8 = [1, 2, 3, 4, 1]
    k8 = 2  # Distance between 1s is 4, which is > 2
    expected8 = False
    result8 = contains_nearby_duplicate(nums8, k8)
    print(f"\nTest 8:")
    print(f"  Input: nums={nums8}, k={k8}")
    print(f"  Output: {result8}")
    print(f"  Expected: {expected8}")
    assert result8 == expected8
    
    # Test case 9: Duplicates exactly at window boundary
    nums9 = [1, 2, 3, 1]
    k9 = 3  # Distance between 1s is 3, which is <= 3
    expected9 = True
    result9 = contains_nearby_duplicate(nums9, k9)
    print(f"\nTest 9:")
    print(f"  Input: nums={nums9}, k={k9}")
    print(f"  Output: {result9}")
    print(f"  Expected: {expected9}")
    assert result9 == expected9
    
    print("\nAll tests passed!")