/*
[Efficient Approach] Using Bitwise AND Operator - O(1) Time and O(1) Space
The last bit of all odd numbers is always 1, while for even numbers it’s 0. So, when performing bitwise AND operation with 1, odd numbers give 1, and even numbers give 0.
*/

#include <stdio.h>

bool isEven(int number) {
    return (number & 1);
}

int main() {
    int n = 15;

    printf(isEven(n) ? "true" : "false");
}
