/*
In the exxpected approach method, sometimes due to large value of n, the value of (n * (n + 1) * (2 * n + 1)) would overflow.
We can avoid this overflow up to some extent using the fact that n*(n+1) must be divisible by 2 and restructuring the formula as (n * (n + 1) / 2) * (2 * n + 1) / 3;
*/

#include <stdio.h>

int sum_of_squares(int number) {
    return number * (number + 1) / 2 * (2 * number + 1) / 3;
}

int main() {
    int number = 3;

    printf("%d", sum_of_squares(number));

    return 0;
}
