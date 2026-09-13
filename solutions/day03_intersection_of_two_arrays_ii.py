"""
LeetCode Problem 350: Intersection of Two Arrays II
Difficulty: Easy
Topics: Array, Hash Table, Two Pointers, Binary Search, Sorting

Problem:
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays 
and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Constraints:
- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 1000

Approach:
Use a hash map to count frequencies of elements in the smaller array,
then iterate through the larger array to find common elements.
Time Complexity: O(n + m) where n and m are lengths of the arrays
Space Complexity: O(min(n, m)) for the hash map
"""

from typing import List
from collections import Counter

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Find the intersection of two arrays with proper frequency counting.
    
    Args:
        nums1: First integer array
        nums2: Second integer array
        
    Returns:
        List containing the intersection with proper frequencies
    """
    # Use the smaller array to build the frequency map for space optimization
    if len(nums1) > len(nums2):
        return intersect(nums2, nums1)
    
    # Count frequencies of elements in the smaller array
    freq_map = Counter(nums1)
    
    # Result list to store intersection
    result = []
    
    # Iterate through the larger array
    for num in nums2:
        # If the number exists in freq_map and count > 0
        if freq_map.get(num, 0) > 0:
            result.append(num)
            freq_map[num] -= 1  # Decrease the count
    
    return result

# Alternative approach using sorting and two pointers
def intersect_sorted(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Alternative approach using sorting and two pointers.
    Time Complexity: O(n log n + m log m)
    Space Complexity: O(1) or O(log n + log m) for sorting
    """
    nums1.sort()
    nums2.sort()
    
    i, j = 0, 0
    result = []
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            # Found a match
            result.append(nums1[i])
            i += 1
            j += 1
    
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1_1 = [1, 2, 2, 1]
    nums2_1 = [2, 2]
    result1 = intersect(nums1_1, nums2_1)
    print(f"Test 1:")
    print(f"  nums1 = {nums1_1}")
    print(f"  nums2 = {nums2_1}")
    print(f"  Result: {sorted(result1)}")  # Expected: [2, 2]
    assert sorted(result1) == [2, 2]
    
    # Test case 2
    nums1_2 = [4, 9, 9, 5]
    nums2_2 = [9, 4, 9, 8, 4]
    result2 = intersect(nums1_2, nums2_2)
    print(f"\nTest 2:")
    print(f"  nums1 = {nums1_2}")
    print(f"  nums2 = {nums2_2}")
    print(f"  Result: {sorted(result2)}")  # Expected: [4, 9]
    assert sorted(result2) == [4, 9]
    
    # Test case 3: No intersection
    nums1_3 = [1, 2, 3]
    nums2_3 = [4, 5, 6]
    result3 = intersect(nums1_3, nums2_3)
    print(f"\nTest 3:")
    print(f"  nums1 = {nums1_3}")
    print(f"  nums2 = {nums2_3}")
    print(f"  Result: {result3}")  # Expected: []
    assert result3 == []
    
    # Test case 4: Empty array
    nums1_4 = []
    nums2_4 = [1, 2, 3]
    result4 = intersect(nums1_4, nums2_4)
    print(f"\nTest 4:")
    print(f"  nums1 = {nums1_4}")
    print(f"  nums2 = {nums2_4}")
    print(f"  Result: {result4}")  # Expected: []
    assert result4 == []
    
    print("\nAll tests passed!")