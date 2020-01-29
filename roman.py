
def to_roman(num):
    # we assert that num is and int and is in range because we cannot represent
    # numbers below 1 or above 3999
    assert isinstance(num, int)
    assert 0 < num < 4000

    arabic = [1, 4, 5, 9, 10, 40, 50, 90,
              100, 400, 500, 900, 1000]
    roman_chars = ["I", "IV", "V", "IX", "X", "XL",
                   "L", "XC", "C", "CD", "D", "CM", "M"]

    i = len(arabic) - 1  # should always be 12
    roman = ""
    while num:
        # this gets us the most significant digit
        digit = num // arabic[i]
        # remove the most significant digit for the next pass
        num %= arabic[i]

        # this appends the desired number of roman numerals to the string
        roman += (roman_chars[i] * digit)

        i -= 1

    return roman
