#include <iostream>
#include <vector>
#include <omp.h>
using namespace std;

int main(int argc, char const *argv[]) {

    int i, n, j, k;
    double time, dot, average;
    for (k=1; k < 9; k++)
    {
        omp_set_num_threads(k);
        for (n = 10,000; n <= 500,000,000; n*=2)
        {
            for (j = 0; j < 10; j++)
            {
                #pragma omp for
                    for(int i=0; i<n; i++) {
                        a[i] = 1./2.;
                        b[i] = double(i+1);
                    }

                time = -omp_get_wtime();
                dot=0.;

                #pragma omp parallel for reduction(+:dot)
                for(int i=0; i<n; i++)
                {
                    dot += a[i] * b[i];
                }
                time += omp_get_wtime();
                average += (time / 10)
            }
            cout << "With" << k << "threads. Average runtime was" << average << '\n';
        }

    }

    return 0;
}
