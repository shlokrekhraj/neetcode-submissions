from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = 0, 0
        res = []

        # use only valid part of nums1 → nums1[:m]
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        # remaining elements
        res.extend(nums1[i:m])
        res.extend(nums2[j:n])

        # copy back into nums1 (IMPORTANT)
        for k in range(m + n):
            nums1[k] = res[k]