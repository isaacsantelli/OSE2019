#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <math.h>
#include <string>
#include <sstream>
// #include <chrono>
// using namespace std::chrono;


using namespace std;


int main()
{
    int steps;
    printf("How many steps would you like to do: ");
    cin >> steps;
    double width = 1.0 / (double) steps;
    int i;
    // auto start = high_resolution_clock::now();
    double rv = 0.0;
    float x, y;
    for (i = 0; i < steps; i++)
    {
        x = i * width;
        y = 4.0 / (1+pow(x,2));
        rv += y * width;
    }
    cout << rv << "\n";
    // auto stop = high_resolution_clock::now();
    // auto duration = duration_cast<seconds>(stop - start);
    // cout << "With " << steps << " iterations the function took " << duration.count() << " seconds \n";
    return rv;
}
