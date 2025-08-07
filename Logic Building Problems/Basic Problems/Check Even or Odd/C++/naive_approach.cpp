/*
Naive Approach] By Finding the Remainder - O(1) Time and O(1) Space
We can check the remainder when divided by 2. If the remainder is 0, the number is even, otherwise it is odd.
*/

#include <iostream>

bool isEven(int number) {
    return (number % 2 == 0);
}

int main()
{
    int n = 15;
    
    if (isEven(n))
        printf("true");
    else
        printf("false");

    return 0;
}