#include <iostream>

using namespace std;

float Double(float x)
{
    return x * 2;
}

int main()
{
    int sum1 = 0;
    int sum2 = 0;
    int sum3 = 0;
    int sum4 = 0; // Creates the integers needed in order to figure out the answer.

    for (int a = 0; a < 1000; a = a + 3)
    {
        sum1 = sum1 + a;
    } // Loops until a is 1000 or over, adding 3 to a every loop. Also adds a to sum1.
    for (int b = 0; b < 1000; b = b + 5)
    {
        sum2 = sum2 + b;
    } // Loops until b is 1000 or over, adding 5 to b every loop. Also adds b to sum2.
    for (int c = 0; c < 1000; c = c + 15)
    {
        sum3 = sum3 + c;
    }                          // Loops until c is 1000 or over, adding 15 to c every loop. Also adds c to sum3.
    sum4 = sum1 + sum2 - sum3; // sum4 takes the sum of sum1 and sum2, and subtracts sum3.
    cout << sum4;              // Outputs sum4, the answer.
    cin.get();                 // Waits for user to press enter.
    return 0;                  // Return statement.
    cout << Double(3);
}
