/*
Using Loop - O(n) Time and O(1) Space
Calculate the sum of all integers from 1 to n by iterating through a loop.
*/

#include <iostream>

int sum_of_integers(int number) {
    // Find the sum of the first n numbers

    int sum = 0, i = 0;

    while (i <= number) {
        sum += i;
        i += 1;
    }
    
    return sum;
}


int main() {
    int number = 3;
    printf("%d", sum_of_integers(number));

    return 0;
}
