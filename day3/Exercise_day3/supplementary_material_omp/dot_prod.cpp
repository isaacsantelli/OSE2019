#include <iostream>
#include <vector>
#include <omp.h>
using namespace std;

int main(void){
    const int N = 100000000;
    vector<double> a(N);
    vector<double> b(N);

    int num_threads = omp_get_max_threads();
    cout << "dot of vectors with length " << N  << " with " << num_threads << " threads" << std::endl;

    // initialize the vectors
    #pragma omp for
        for(int i=0; i<N; i++) {
            a[i] = 1./2.;
            b[i] = double(i+1);
        }

    double time = -omp_get_wtime();
    double dot=0.;

    #pragma omp parallel for reduction(+:dot)
    for(int i=0; i<N; i++)
    {
        dot += a[i] * b[i];
    }
    time += omp_get_wtime();

    // use formula for sum of arithmetic sequence: sum(1:n) = (n+1)*n/2
    double expected = double(N+1)*double(N)/4.;
    cout << "dot product " << dot
              << (dot==expected ? " which matches the expected value "
                                : " which does not match the expected value ")
              << expected << endl;
    cout << "that took " << time << " seconds" << std::endl;
    return 0;
}
