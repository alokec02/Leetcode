class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        p = []
        greater = []
        for n in nums:
            if n < pivot:
                less.append(n)
            elif n==pivot:
                p.append(n)
            else:
                greater.append(n)
        return less + p + greater
