"""
Expected Approach Without using Third Variable
The idea is to swap two numbers using Arithmetic operators or Bitwise operators.
"""

#include <iostream>

int main() {
    int a = 2, b = 3;

    printf("a = %d; b = %d\n", a, b);
  
    std::swap(a, b);
  
    printf("a = %d; b = %d", a, b);

    return 0;
}
