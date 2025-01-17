#include<stdio.h>
int main(){
    int N, K, X;
    int i;

    scanf("%d %d %d", &N, &K, &X);

    int A[N];

    for(i = 0; i < N; i++){
        scanf("%d", &A[i]);
    }
    i = 0;
    do{
        printf("%d ", A[i]);
        i++;
        if(i == K){
            printf("%d ", X);
        }
    }while(i < N);
    return 0;
}