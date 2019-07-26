#include <iostream>
#include <vector>
#include <omp.h>
using namespace std;

int main(void) {
    int i, n, j, k;
    double time, dot, average;
    for (k=1; k < 9; k++)
    {
	cout << "test \n";
        omp_set_num_threads(k);
        for (n = 10000; n <= 500000000; n*=2)
        {
	//cout << "test \n";
            vector<double> a(n);
            vector<double> b(n);
            for (j = 0; j < 10; j++)
            {
                #pragma omp for
                    for(int i=0; i<n; i++) {
                        a[i] = 1./2.;
                        b[i] = double(i+1);
                    }
	//cout << "test \n";
		time = 0;
                time = -omp_get_wtime();
                dot=0.;

                #pragma omp parallel for reduction(+:dot)
                for(int i=0; i<n; i++)
                {
                    dot += a[i] * b[i];
                }
                time += omp_get_wtime();
                average += (time / 10);
            }
            cout << "With " << k << " threads and " << n << " entries \n";
	    cout << "Average runtime was " << average << '\n';
        
	average = 0;
	}

    }

    return 0;
}
