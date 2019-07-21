#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    float a, b, c;
    printf("What value would you like to use for a: ");
    cin >> a;
    printf("What value would you like to use for b: ");
    cin >> b;
    printf("What value would you like to use for c: ");
    cin >> c;

    float x1, x2;
    x1 = (-b + pow((pow(b, 2) - 4*a*c), .5) ) / (2*a);
    x2 = (-b - pow((pow(b, 2) - 4*a*c), .5) ) / (2*a);
    cout << "x1 is: " << x1 << "\n";
    if (x1 != x2) cout << "x2 is:" << x2 << "\n";

}
