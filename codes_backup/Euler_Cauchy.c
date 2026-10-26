#include <stdio.h>

int main() {
    double t_max = 0.5;
    double y_max = t_max - t_max * t_max;
    printf("Maximum value of y(t) over [0,1] is: %.2f\n", y_max);
    return 0;
}
