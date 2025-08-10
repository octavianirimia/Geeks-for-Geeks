"""
So we want to find out the √n

Let's say x is the result of √n
x = √n

Let's square both sides
x² = n

Let's apply log to both sides
log(x²) = log(n)

2 * log(x) = log(n)

log(x) = ½ log(n)

Apply e to both sides

e ^ (log(x)) = e ^ ½ log(n)

x = e ^ ½ log(n)

And who is x? x is √n

So

√n = e ^ ½ log(n)


NOTE:
Because of the way computations are done in computers in case of decimals, the result from the expression may be slightly less than the actual square root.
Therefore, we will also consider the next integer after the calculated result as a potential answer.
"""

from math import exp, log


def floor_sqrt(number: int) -> int:
    number_sqrt: int = int(exp(1/2 * log(number)))

    if (number_sqrt + 1) ** 2 <= number:
        return number_sqrt + 1
    
    return number_sqrt


if __name__ == "__main__":
    print(floor_sqrt(10453))