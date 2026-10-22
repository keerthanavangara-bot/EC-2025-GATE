#include <stdio.h>

int main() {
    int SEL[] = {0, 1, 1, 0}, S[] = {0, 0, 1, 1};
    int Q1 = 0, Q2 = 1;
    printf("Time | SEL S | Q1 Q2 | Y\n");
    for (int i = 0; i < 4; i++) {
        int Y = Q1 ^ Q2;
        printf(" T%d  |  %d   %d |  %d  %d  | %d\n", i, SEL[i], S[i], Q1, Q2, Y);
        Q1 = SEL[i] ? S[i] : 0;
        Q2 = SEL[i] ? Q1   : 1;
    }
    return 0;
}
