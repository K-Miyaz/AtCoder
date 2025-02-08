#include<stdio.h>
#include<string.h>

int main(){
    int len, hide_bool = 0;
    char S[105];

    scanf("%s", &S);
    len = strlen(S);
    for(int i = 0; i < len; ++i){
        if(S[i] == ('|')){
            if(hide_bool == 0) hide_bool = 1;
            else hide_bool = 0;
            continue;
        }
        if(hide_bool == 0){
            printf("%c", S[i]);
        }
    }
    printf("\n");
    return 0;
}