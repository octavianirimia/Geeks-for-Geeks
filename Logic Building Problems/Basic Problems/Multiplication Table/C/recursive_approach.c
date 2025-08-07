/*
In this method, we pass i as an additional parameter with initial value as 1. We print n * i and then recursively call for i+1.
We stop the recursion when i becomes 11 as we need to print only 10 multiples of given number and i.
*/

#include <stdio.h>

void printMultiplicationTable(int number, int i) {
    // Print the multiplication table recursively
    if (i == 11)
        return;

    printf("%d x %d = %d\n", number, i, number * i);

    printMultiplicationTable(number, ++i);
}

int main() {
    int number = 5;

    printMultiplicationTable(number, 1);
}
