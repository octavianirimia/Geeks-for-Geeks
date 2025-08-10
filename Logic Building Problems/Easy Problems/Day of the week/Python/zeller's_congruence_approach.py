"""
This approach calculates the day of the week for a given date using a formula involving the year, month, and day. It is essentially a simplified version of Zeller's Congruence, with adjustments for century years and leap years.

Predefined Month Codes (t[]):
The array t[] stores month codes for each month. These values are predefined to account for the different lengths of each month.
For example: January = 6, February = 2 (or 1 for leap years), March = 2, etc.
Adjusting the Year for January and February (y -= m < 3):
The code adjusts the year if the month is January or February.
This is because in Zeller's Congruence, January and February are treated as the 13th and 14th months of the previous year.
If the month is January or February, it reduces the year by 1 (i.e., y -= 1).
Leap Year Adjustments (y / 4 - y / 100 + y / 400): The formula adjusts for leap years and century years:
y / 4: Adds an adjustment for the leap years.
y / 100: Subtracts the days for century years that are not leap years.
y / 400: Adds back the leap days for century years that are divisible by 400 (e.g., 1600, 2000).
Final Calculation:
The formula: (y + y/4 − y/100 + y/400 + t[m−1] + d) % 7 calculates the day of the week by summing the day (d), month code (t[m - 1]), and adjusted year values.
The result is then taken modulo 7, which gives a value between 0 and 6, corresponding to the days of the week: 0 = Sunday, 1 = Monday, ..., 6 = Saturday.
"""

def month_code(month: int, year: int) -> int:
    """Return the month code for the given month and year."""
    codes = {
        1: 0,  2: 3,  3: 3,  4: 6,
        5: 1,  6: 4,  7: 6,  8: 2,
        9: 5, 10: 0, 11: 3, 12: 5
    }
    code = codes[month]
    # Adjust for leap year in Jan and Feb
    if month in (1, 2) and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        code = (code - 1) % 7
    return code

# Example
print(month_code(3, 2025))  # March 2025 → 3
print(month_code(2, 2024))  # February 2024 (leap year) → 2
