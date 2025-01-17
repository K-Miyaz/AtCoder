#include<stdio.h>
#include<string.h>

int main(){
    int N, ans = 1;
    char S_befor[100];
    char S_after[100];
    char sweet[100] = "sweet";

    scanf("%d", &N);
    scanf("%s", S_befor);
    for(int i = 1; i < N; i++){
        scanf("%s", S_after);
        if(strcmp(S_after, S_befor) == 0){
            if(strcmp(S_after, sweet) == 0){
                ans = 0;
                if(i == N - 1){
                    ans = 1;
                }
                break;
            }
        }
        strcpy(S_befor, S_after);
    }
    if(ans == 1){
        printf("Yes");
    }
    else{
        printf("No");
    }
    return 0;
}