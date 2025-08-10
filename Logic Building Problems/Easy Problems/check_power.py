"""
Logarithmic Method
This approach checks if y is a power of x using logarithms.
By applying the logarithm change of base formula, it computes log⁡y(x)=log⁡(y)/log⁡(x).
If the result is an integer, it means that y is an exact power of x, and the function returns true.
Otherwise, it returns false.
"""

from math import log

def is_power(x: int, y: int) -> bool:
    """Check if y is a power of x"""
    if x <= 1 or y < 1:
        return False
    
    log_result = log(y) / log(x)
    
    return log_result.is_integer()

if __name__ == "__main__":
    print(is_power(2, 128))
