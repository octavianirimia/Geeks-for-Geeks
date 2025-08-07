/*
By finding Quotient - O(1) Time and O(1) Space
We first compute the quotient q = n / m, then calculate two candidates:

n1 = m * q
 This is the closest multiple of m that is less than or equal to n.
n2 = m * (q + 1) or m * (q - 1)
 We choose q + 1 or q - 1 based on the signs of n and m:
If n and m have the same sign, use n2 = m * (q + 1)
 This moves in the direction toward n, getting the next closest multiple above n.
If n and m have opposite signs, use n2 = m * (q - 1)
 This accounts for the fact that increasing q would move away from n due to the sign flip, so we instead go backward to get the next closest multiple.
Then we return the one (n1 or n2) that has the smaller absolute difference from n.

If both have the same distance from n, return the one with the greater absolute value, as required.
*/

#include <stdio.h>

int closestNumber(int n, int m) {
    int q = n / m;
    int n1 = m * q, n2 = (n * m > 0) ? (m * (q + 1)) : (m * (q - 1));

    return (abs(n - n1) < abs(n - n2)) ? n1 : n2;
}

int main() {
    int n = -15, m = 6;

    printf("%d", closestNumber(n, m));
}
