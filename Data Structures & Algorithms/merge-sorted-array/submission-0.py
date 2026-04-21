class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        L = nums1[:m]
        R = nums2

        k = 0
        i = 0
        j = 0

        while i < len(L) and j < len(R):
            if R[j] >= L[i]:
                nums1[k] = L[i]
                i += 1
            else:
                nums1[k] = R[j]
                j += 1
            k += 1
        
        # los que sobren de ambos lados
        while i < len(L):
            nums1[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            nums1[k] = R[j]
            j += 1
            k += 1
