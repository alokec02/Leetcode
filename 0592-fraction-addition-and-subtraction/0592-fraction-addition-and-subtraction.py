from fractions import Fraction
import re
class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = [Fraction(token) for token in re.findall(r'[+-]?\d+/\d+', expression)]
        return f"{sum(fractions).numerator}/{sum(fractions).denominator}"

