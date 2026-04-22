class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for array in matrix:
            L, R = 0, len(array) - 1

            while L <= R:
                mid = (L + R) // 2
                if target > array[mid]:
                    L = mid + 1
                elif target < array[mid]:
                    R = mid - 1
                else:
                    return True
        return False