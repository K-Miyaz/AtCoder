#include<stdio.h>
#include<string.h>

int main(){
    int N, ans = 0;

    scanf("%d", &N);
    for(int i = 0; i < N; i++){
        char S[100];
        scanf("%s", S);
        if(strcmp(S, "Takahashi") == 0){
            ans++;
        }
    }
    printf("%d",ans);

    return 0;
}