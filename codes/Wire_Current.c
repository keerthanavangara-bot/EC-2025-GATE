#include <stdio.h>
#define PI 3.14159265358979323846

int main() {
    double E = 0.01, sigma = 5.8e7, d = 1e-3;
    double r = d / 2.0;
    double A = PI * r * r;
    double I = sigma * E * A;
    printf("Current I = %.2f A\n", I);
    return 0;
}
