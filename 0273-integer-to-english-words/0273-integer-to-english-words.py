class Solution:
    def numberToWords(self, num: int) -> str:
        # Check for the zero case explicitly
        if num == 0:
            return 'Zero'

        # Words for numbers less than 20
        less_than_20 = [
            '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
            'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
            'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
        ]
      
        # Tens place words
        tens = [
            '', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'
        ]
      
        # Units of thousand
        thousands = ['Billion', 'Million', 'Thousand', '']

        # Helper function to convert a number less than 1000 to words
        def translate(num):
            if num == 0:
                return ''
            elif num < 20:
                return less_than_20[num] + ' '
            elif num < 100:
                return tens[num // 10] + ' ' + translate(num % 10)
            else:
                return less_than_20[num // 100] + ' Hundred ' + translate(num % 100)

        result = []  # List to store the parts of the result string
        i, j = 1000000000, 0  # Initialize the divisor for the highest unit (billion) and the index for units
      
        # Loop to handle each unit position from billion down to ones
        while i > 0:
            if num // i != 0:
                result.append(translate(num // i))  # Convert the current unit position to words
                result.append(thousands[j])         # Add the unit name (Billion, Million, ...)
                result.append(' ')                  # Add space after the unit name
                num %= i                            # Update the number, removing the current unit portion
            j += 1  # Increment the index for units
            i //= 1000  # Move to the next unit (from billion to million to thousand to ones)
      
        return ''.join(result).strip()  # Convert the list to a string and remove any leading/trailing space
