#include<stdio.h>

int main(){
    int N, L, R;
    int j = 0;

    scanf("%d %d %d",&N ,&L, &R);
    for(int i = 1; i <= N; i++){
        if((i >= L) && (i <= R)){
            printf("%d ", R - j);
            j++;
        }
        else{
            printf("%d ", i);
        }
    }
    return 0;
}