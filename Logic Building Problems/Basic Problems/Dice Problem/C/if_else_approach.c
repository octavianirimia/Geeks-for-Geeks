/*
Using if-else Statement
In a normal 6-faced dice, 1 is opposite to 6, 2 is opposite to 5, and 3 is opposite to 4. Hence a normal if-else-if block can be placed
*/

#include <stdio.h>

int oppositeFaceOfDice(int n) {
    if (n == 1)
        return 6;
    if (n == 2)
        return 5;
    if (n == 3)
        return 4;
    if (n == 4)
        return 3;
    if (n == 5)
        return 2;
    return 1;
}

int main() {
    int n = 2;
    printf("%d", oppositeFaceOfDice(2));
}
