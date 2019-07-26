#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <math.h>
#include <string>
#include <sstream>
// #include <chrono>
// using namespace std::chrono;


using namespace std;

int func1(float x, float y);

int func1(float x, float y)
{
    if (pow(x,2) + pow(y, 2) <= 1) return 4;
    else return 0;
}

int main() {

    int iterations;
    printf("How many iterations would you like to do: ");
    cin >> iterations;
    int i;
    float x, y;
    double rv = 0.0;
    // auto start = high_resolution_clock::now();

    #pragma omp parallel for reduction(+:rv)
    for (i = 0; i < iterations; i++)
    {
        x = static_cast <float> (rand()) / static_cast <float> (RAND_MAX/2) - 1;
        y = static_cast <float> (rand()) / static_cast <float> (RAND_MAX/2) - 1;
        rv += float(func1(x, y)) / iterations;
    }
    cout << rv << "\n";
    //auto stop = high_resolution_clock::now();
    //auto duration = duration_cast<seconds>(stop - start);
    //cout << "With " << iterations << " iterations the function took " << duration.count() << " seconds \n";
    return rv;
}
