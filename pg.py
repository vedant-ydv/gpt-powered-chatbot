def search_rotated_array(arr: list[int], target: int) -> int:
    """
    Find the index of target element in a sorted rotated array.
    Returns -1 if element is not found.
    
    Example:
    arr = [4, 5, 6, 7, 0, 1, 2, 3]  # sorted array [0,1,2,3,4,5,6,7] rotated 4 times
    target = 0
    returns: 4 (index of target element)
    """
    if not arr:
        return -1
        
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
            
        # Check if left half is sorted
        if arr[left] <= arr[mid]:
            # Check if target lies in left half
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half must be sorted
        else:
            # Check if target lies in right half
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1

def test_search_rotated_array():
    """Test cases for search_rotated_array function"""
    # Test case 1: Normal rotated array
    arr1 = [4, 5, 6, 7, 0, 1, 2, 3]
    assert search_rotated_array(arr1, 0) == 4
    assert search_rotated_array(arr1, 3) == 7
    assert search_rotated_array(arr1, 5) == 1
    
    # Test case 2: Not rotated array
    arr2 = [1, 2, 3, 4, 5]
    assert search_rotated_array(arr2, 3) == 2
    
    # Test case 3: Single rotation
    arr3 = [2, 3, 4, 5, 1]
    assert search_rotated_array(arr3, 1) == 4
    
    # Test case 4: Element not present
    assert search_rotated_array(arr3, 6) == -1
    
    # Test case 5: Empty array
    assert search_rotated_array([], 5) == -1
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Example usage
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    target = 0
    result = search_rotated_array(arr, target)
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"Found at index: {result}")
    
    # Run tests
    test_search_rotated_array()
