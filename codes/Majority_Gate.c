#include <stdio.h>

int main() {
    printf("X Y Z | F\n---------\n");
    for (int x = 0; x <= 1; x++) {
        for (int y = 0; y <= 1; y++) {
            for (int z = 0; z <= 1; z++) {
                int F = (x & y) | (y & z) | (z & x);
                printf("%d %d %d | %d\n", x, y, z, F);
            }
        }
    }
    return 0;
}
