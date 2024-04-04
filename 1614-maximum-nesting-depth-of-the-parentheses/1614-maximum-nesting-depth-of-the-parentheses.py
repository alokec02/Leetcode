class Solution:
    def maxDepth(self, s: str) -> int:
      import math
      Counter = 0
      MaxCounter = 0
      for i in range(len(s)):
        if s[i]=="(":
            Counter+=1
            MaxCounter = max(MaxCounter, Counter) 
        if s[i] == ")":
            Counter-=1
      return MaxCounter  