#include <stdio.h>

int main() {
    int z = 1;
    printf("X Y Z | Sum (F) | Expected\n");
    
    
    for (int x = 0; x <= 1; x++) {
        for (int y = 0; y <= 1; y++) {
            int xor_out = y ^ z;
            int sum = x ^ xor_out ^ z;
            int expected = (x - y < 0) ? (x - y + 2) : (x - y);
            
            printf("%d %d %d |    %d    |    %d\n", x, y, z, sum, expected);
        }
    }
    return 0;
}
