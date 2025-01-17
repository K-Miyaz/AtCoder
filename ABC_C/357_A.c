#include<stdio.h>

int main(){
    int N, M;
    int H[101];
    int i;

    scanf("%d %d",&N ,&M);
    for(i = 0; i < N; i++){
        scanf("%d",&H[i]);
    }

    for(i = 0; i < N; i++){
        M -= H[i];
        if(M < 0){
            break;
        }
    }
    printf("%d",i);
    return 0;
}