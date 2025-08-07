/*
Using Sum of Two Sides
The idea is based on the observation that the sum of two opposite sides of a cubical dice is equal to 7. So, just subtract the given n from 7 and print the answer.
*/

    #include <iostream>

    int oppositeFaceOfDice(int n) {
        return 7 - n;
    }

    int main() {
        int n = 2;
        printf("%d", oppositeFaceOfDice(n));
    }
