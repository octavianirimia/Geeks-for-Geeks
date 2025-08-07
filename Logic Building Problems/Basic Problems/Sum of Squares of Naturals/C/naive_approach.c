/*
Naive Approach - Adding One By One - O(n) Time and O(1) Space
The idea for this naive approach is to run a loop from 1 to n and sum up all the squares.
*/

#include <stdio.h>

int sum_of_squares(int number) {
    // Return the sum of the squared numbers from 1 to n

    int sum_of_squares = 0;
    
    for (int i = 0; i <= number; i++)
        sum_of_squares += i * i;

    return sum_of_squares;
}


int main() {
    int number = 3;

    printf("%d", sum_of_squares(number));

    return 0;
}
