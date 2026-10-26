#include <stdio.h>
#include <math.h>

int main() {
    double p_xy[2][2] = {{0.06, 0.14}, {0.24, 0.56}};
    double px[2] = {0.20, 0.80}, py[2] = {0.30, 0.70};
    double I = 0.0;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            if (p_xy[i][j] > 0) {
                I += p_xy[i][j] * log2(p_xy[i][j] / (px[i] * py[j]));
            }
        }
    }
    printf("Mutual Information I(X;Y) = %.2f bits\n", I);
    return 0;
}
