#include<stdio.h>

int main(){
    int N;
    int A[100];

    scanf("%d", &N);
    for(int i = 0; i < N; i++){
        scanf("%d", &A[i]);
    }
    for(int i = 0; i < N - 1; i++){
        printf("%d ", A[i] * A[i + 1]);
    }
    printf("\n");

    return 0;
}