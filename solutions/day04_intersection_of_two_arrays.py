"""
LeetCode Problem 349: Intersection of Two Arrays
Difficulty: Easy
Topics: Array, Hash Table, Two Pointers, Binary Search, Sorting

Problem:
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:
- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 1000

Approach:
Use sets to eliminate duplicates and find intersection efficiently.
Time Complexity: O(n + m) where n and m are lengths of the arrays
Space Complexity: O(n + m) for the two sets
"""

from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Find the intersection of two arrays with unique elements only.
    
    Args:
        nums1: First integer array
        nums2: Second integer array
        
    Returns:
        List containing the unique intersection elements
    """
    # Convert both arrays to sets to eliminate duplicates
    set1 = set(nums1)
    set2 = set(nums2)
    
    # Find intersection using set operation
    result_set = set1 & set2  # Equivalent to set1.intersection(set2)
    
    # Convert back to list
    return list(result_set)

# Alternative approach using hash map
def intersection_hashmap(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Alternative approach using hash map for educational purposes.
    """
    # Use the smaller array to build the hash set
    if len(nums1) > len(nums2):
        return intersection_hashmap(nums2, nums1)
    
    # Create a set from the smaller array
    num_set = set(nums1)
    
    # Use another set to avoid duplicates in result
    result_set = set()
    
    # Check each element in the larger array
    for num in nums2:
        if num in num_set:
            result_set.add(num)
    
    return list(result_set)

# Alternative approach using sorting and two pointers
def intersection_sorted(nums1: List[int], nums2: List[int]) -> List[int]:
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
        # Skip duplicates in nums1
        if i > 0 and nums1[i] == nums1[i-1]:
            i += 1
            continue
        # Skip duplicates in nums2
        if j > 0 and nums2[j] == nums2[j-1]:
            j += 1
            continue
            
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
    result1 = intersection(nums1_1, nums2_1)
    print(f"Test 1:")
    print(f"  nums1 = {nums1_1}")
    print(f"  nums2 = {nums2_1}")
    print(f"  Result: {sorted(result1)}")  # Expected: [2]
    assert sorted(result1) == [2]
    
    # Test case 2
    nums1_2 = [4, 9, 5]
    nums2_2 = [9, 4, 9, 8, 4]
    result2 = intersection(nums1_2, nums2_2)
    print(f"\nTest 2:")
    print(f"  nums1 = {nums1_2}")
    print(f"  nums2 = {nums2_2}")
    print(f"  Result: {sorted(result2)}")  # Expected: [4, 9]
    assert sorted(result2) == [4, 9]
    
    # Test case 3: No intersection
    nums1_3 = [1, 2, 3]
    nums2_3 = [4, 5, 6]
    result3 = intersection(nums1_3, nums2_3)
    print(f"\nTest 3:")
    print(f"  nums1 = {nums1_3}")
    print(f"  nums2 = {nums2_3}")
    print(f"  Result: {result3}")  # Expected: []
    assert result3 == []
    
    # Test case 4: One empty array
    nums1_4 = []
    nums2_4 = [1, 2, 3]
    result4 = intersection(nums1_4, nums2_4)
    print(f"\nTest 4:")
    print(f"  nums1 = {nums1_4}")
    print(f"  nums2 = {nums2_4}")
    print(f"  Result: {result4}")  # Expected: []
    assert result4 == []
    
    # Test case 5: Duplicates in both arrays
    nums1_5 = [1, 1, 2, 2, 3, 3]
    nums2_5 = [2, 2, 3, 3, 4, 4]
    result5 = intersection(nums1_5, nums2_5)
    print(f"\nTest 5:")
    print(f"  nums1 = {nums1_5}")
    print(f"  nums2 = {nums2_5}")
    print(f"  Result: {sorted(result5)}")  # Expected: [2, 3]
    assert sorted(result5) == [2, 3]
    
    print("\nAll tests passed!")