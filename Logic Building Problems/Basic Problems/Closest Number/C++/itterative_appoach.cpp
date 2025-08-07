/*
Iterative Checking - O(m) Time and O(1) Space
The basic idea is to start checking from n - m to n + m one by one and take the closest number.
*/

#include <iostream>
#include <climits>

int closestNumber(int n, int m) {
    int closest = 0, minimumDiffernce = INT_MAX;

    for (int i = n - abs(m); i <= n + abs(m); i++)
        if (!(i % m)) {
            int difference = abs(n - i);

            if (difference < minimumDiffernce || (difference == minimumDiffernce && abs(i) > abs(closest))) {
                closest = i;
                minimumDiffernce = difference;
            }
        }
    
    return closest;
}

int main() {
    int n = -15, m = 6;

    printf("%d", closestNumber(n, m));

    return 0;
}
