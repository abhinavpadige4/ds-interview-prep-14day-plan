"""
LeetCode Problem 347: Top K Frequent Elements
Difficulty: Medium
Topics: Array, Hash Table, Divide and Conquer, Heap (Priority Queue), Bucket Sort, Counting, Sorting

Problem:
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 10^5
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

Approach:
Use bucket sort (frequency-based approach):
1. Count frequencies of each element using hash map
2. Create buckets where index represents frequency
3. Place elements in buckets according to their frequency
4. Collect results from highest frequency buckets down to get top k
Time Complexity: O(n) - linear time
Space Complexity: O(n) - for hash map and buckets
"""

from typing import List
from collections import Counter

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find the k most frequent elements in the array.
    
    Args:
        nums: List of integers
        k: Number of top frequent elements to return
        
    Returns:
        List of k most frequent elements
    """
    # Count frequencies of each element
    freq_map = Counter(nums)
    
    # Create buckets: index = frequency, value = list of elements with that frequency
    # Maximum frequency can be len(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    
    # Place elements in buckets according to their frequency
    for num, freq in freq_map.items():
        buckets[freq].append(num)
    
    # Collect results from highest frequency buckets down
    result = []
    for freq in range(len(buckets) - 1, 0, -1):  # From high to low frequency
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:  # We've collected k elements
                return result
    
    return result  # Should never reach here per problem constraints

# Alternative approach using heap (priority queue)
def top_k_frequent_heap(nums: List[int], k: int) -> List[int]:
    """
    Alternative approach using min-heap.
    Time Complexity: O(n log k)
    Space Complexity: O(n)
    """
    import heapq
    
    # Count frequencies
    freq_map = Counter(nums)
    
    # Use min-heap to keep track of top k elements
    # We store (-frequency, element) to simulate max-heap behavior
    heap = []
    for num, freq in freq_map.items():
        heapq.heappush(heap, (-freq, num))
    
    # Extract top k elements
    result = []
    for _ in range(k):
        if heap:
            result.append(heapq.heappop(heap)[1])
    
    return result

# Alternative approach using sorting
def top_k_frequent_sort(nums: List[int], k: int) -> List[int]:
    """
    Alternative approach using sorting.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    # Count frequencies
    freq_map = Counter(nums)
    
    # Sort by frequency (descending) and take top k
    sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
    
    # Extract just the elements
    return [item[0] for item in sorted_items[:k]]

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    expected1 = [1, 2]  # Order doesn't matter
    result1 = top_k_frequent(nums1, k1)
    print(f"Test 1:")
    print(f"  Input: nums={nums1}, k={k1}")
    print(f"  Output: {sorted(result1)}")
    print(f"  Expected: {sorted(expected1)}")
    assert sorted(result1) == sorted(expected1)
    
    # Test case 2
    nums2 = [1]
    k2 = 1
    expected2 = [1]
    result2 = top_k_frequent(nums2, k2)
    print(f"\nTest 2:")
    print(f"  Input: nums={nums2}, k={k2}")
    print(f"  Output: {result2}")
    print(f"  Expected: {expected2}")
    assert result2 == expected2
    
    # Test case 3: All same elements
    nums3 = [5, 5, 5, 5]
    k3 = 1
    expected3 = [5]
    result3 = top_k_frequent(nums3, k3)
    print(f"\nTest 3:")
    print(f"  Input: nums={nums3}, k={k3}")
    print(f"  Output: {result3}")
    print(f"  Expected: {expected3}")
    assert result3 == expected3
    
    # Test case 4: All different elements
    nums4 = [1, 2, 3, 4, 5]
    k4 = 3
    expected4 = [1, 2, 3]  # Any 3 elements
    result4 = top_k_frequent(nums4, k4)
    print(f"\nTest 4:")
    print(f"  Input: nums={nums4}, k={k4}")
    print(f"  Output: {sorted(result4)}")
    print(f"  Expected: {sorted(expected4)}")
    assert sorted(result4) == sorted(expected4)
    
    # Test case 5: k equals number of unique elements
    nums5 = [1, 1, 2, 2, 3, 3]
    k5 = 3
    expected5 = [1, 2, 3]
    result5 = top_k_frequent(nums5, k5)
    print(f"\nTest 5:")
    print(f"  Input: nums={nums5}, k={k5}")
    print(f"  Output: {sorted(result5)}")
    print(f"  Expected: {sorted(expected5)}")
    assert sorted(result5) == sorted(expected5)
    
    # Test case 6: Large k
    nums6 = [1, 2, 2, 3, 3, 3]
    k6 = 2
    expected6 = [2, 3]  # 2 appears twice, 3 appears three times
    result6 = top_k_frequent(nums6, k6)
    print(f"\nTest 6:")
    print(f"  Input: nums={nums6}, k={k6}")
    print(f"  Output: {sorted(result6)}")
    print(f"  Expected: {sorted(expected6)}")
    assert sorted(result6) == sorted(expected6)
    
    # Test case 7: Single element repeated
    nums7 = [1]
    k7 = 1
    expected7 = [1]
    result7 = top_k_frequent(nums7, k7)
    print(f"\nTest 7:")
    print(f"  Input: nums={nums7}, k={k7}")
    print(f"  Output: {result7}")
    print(f"  Expected: {expected7}")
    assert result7 == expected7
    
    print("\nAll tests passed!")