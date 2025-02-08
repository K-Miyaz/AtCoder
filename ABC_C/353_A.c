#include<stdio.h>

int main(){
    int N, ans = -1, i;
    int H[100];

    scanf("%d",&N);
    for(i = 0; i < N; i++){
        scanf("%d",&H[i]);
    }
    for(i = 1; i < N; i++){
        if(H[i] > H[0]){
            ans = i + 1;
            break;
        }
    }
    printf("%d", ans);
    return 0;
}