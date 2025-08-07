/*
Expected Approach - Using Mathematical Formulae - O(1) Time and O(1) Space
The idea for this approach is to use the mathematical formulae for the sum of squares of first n natural numbers.

12 + 22 + ......... + n2 = n(n+1)(2n+1) / 6

We can prove this formula using induction. We can easily see that the formula is true for n = 1 and n = 2 as sums are 1 and 5 respectively.

Let it be true for n = k-1. So sum of k-1 numbers
is (k – 1) * k * (2 * k – 1)) / 6

In the following steps, we show that it is true
for k assuming that it is true for k-1.

Sum of k numbers = Sum of k-1 numbers + k2
           = (k – 1) * k * (2 * k – 1) / 6 + k2
           = ((k2 – k) * (2*k – 1) + 6k2)/6
           = (2k3 – 2k2 – k2 + k + 6k2)/6
           = (2k3 + 3k2 + k)/6
           = k * (k + 1) * (2*k + 1) / 6
*/

#include <iostream>

int sum_of_squares(int number) {
    return number * (number + 1) * (2 * number + 1) / 6;
}

int main() {
    int number = 3;

    printf("%d", sum_of_squares(number));

    return 0;
}
