/*
The iterative approach for printing a multiplication table involves using a loop to calculate and print the product of a given number and the numbers in range from 1 to 10.
In this method, you begin with the number whose table you want to print and use a loop to multiply it with increasing values.
*/

#include <iostream>

void printMultiplicationTable(int number) {
    // Print the multiplication table

    for (int i = 1; i <= 10; i++)
        printf("%d x %d = %d\n", number, i, number * i);
}

int main() {
    int number = 5;
    printMultiplicationTable(number);

    return 0;
}
