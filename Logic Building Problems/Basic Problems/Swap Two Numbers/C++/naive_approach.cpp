/*
Naive Approach Using Third Variable
The idea is to use a third variable, say temp to store the original value of one of the variables during the swap.

Store the value of a in temp.
Assign the value of b to a.
Assign the value of temp to b.
*/

#include <iostream>

int main() {
    int a = 2, b = 3;

    printf("a = %d; b = %d\n", a, b);
  
    int temp = a;
    a = b;
    b = temp;
  
    printf("a = %d; b = %d", a, b);

    return 0;
}
