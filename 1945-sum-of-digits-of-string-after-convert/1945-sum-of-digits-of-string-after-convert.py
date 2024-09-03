class Solution:
    def getLucky(self, s: str, k: int) -> int:
        c = []
        for x in s:
            c.append(str(ord(x) - ord('a') + 1))

        s = "".join(c)
        for _ in range(k):
            total = 0

            for x in s:
                total += int(x)
            s = str(total)
        return int(s)