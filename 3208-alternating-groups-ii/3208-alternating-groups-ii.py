class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        n = len(colors)
        left = ans = 0

        for right in range(1, n + k - 1):
            if colors[right % n] == colors[(right - 1) % n]:
                left = right

            if right - left + 1 == k:
                ans += 1
                left += 1

        return ans
        