"""
我们把符合下列属性的数组 A 称作山脉：
A.length >= 3
存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。

示例 1：
输入：[0,1,0]
输出：1

示例 2：
输入：[0,2,1,0]
输出：1
 
提示：
3 <= A.length <= 10000
0 <= A[i] <= 10^6
A 是如上定义的山脉
"""


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l = 0
        r = len(A) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if mid + 1 <= r and A[mid] > A[mid + 1]:
                return A[mid]
            if mid - 1 >= l and A[mid] < A[mid - 1]:
                return A[mid - 1]
            if A[mid] < A[0]:
                r = mid - 1
            if A[mid] > A[-1]:
                l = mid + 1
            else:
                return mid

