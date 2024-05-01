class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        indexCh = word.index(ch)
        return word[indexCh::-1]+word[indexCh+1::1]



            
