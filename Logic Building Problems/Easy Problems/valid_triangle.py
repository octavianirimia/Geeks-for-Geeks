"""
A triangle is valid if sum of its two sides is greater than the third side.
If three sides are a, b and c, then three conditions should be met. 
"""

def valid_triangle(a: int, b: int, c: int) -> bool:

    if a + b <= c or a + c <= b or b + c <= a:
        return False
    
    return True


if __name__ == "__main__":
    print(valid_triangle(7, 10, 5))
