#include <stdio.h>

int main() {
    double t_cq = 2.0, t_and = 1.0, t_setup = 2.0;
    double T_min = t_cq + t_and + t_setup;
    double f_max = (1.0 / T_min) * 1000.0;
    printf("Minimum Clock Period = %.1f ns\n", T_min);
    printf("Maximum Clock Frequency = %.0f MHz\n", f_max);
    return 0;
}
