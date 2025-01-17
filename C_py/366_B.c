#include<stdio.h>
int main(){
    int i = 0, j = 0;
    int N, max = 0,max_i, Ssize[100];
    char* S[100][100];

    scanf("%d", &N);
    for(i = 0; i < N; i++){
        scanf("%s", S[i]);
        // 配列の要素数を調べる
        Ssize[i] = sizeof S[i] /sizeof S[i][0];
        if(Ssize[i] > max){
            max = Ssize[i];
            max_i = i;
        }
    }

    while(j < max){
        for(i = N - 1; i >= 0; i--){
            if(j >= Ssize[i]){
                if((j == max - 1) && (max_i > i)){
                    break;
                }
                printf("*");
            }
            else{
                printf("%s", S[i][j]);
            }
        }
        j++;
        printf("\n");
    }
}