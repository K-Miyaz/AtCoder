#include<stdio.h>
#include<string.h>

int main(){
    int ok = 1, len;
    char S[101];

    scanf("%s", &S);
    len = strlen(S);
    if(S[0] != '<' || S[len - 1] != '>'){
        ok = 0;
    }
    for(int i = 1; i < len - 1; ++i){
        if(S[i] != '='){
            ok = 0;
            break;
        }
    }
    if(ok == 1){
        printf("Yes\n");
    }
    else{
        printf("No\n");
    }

    return 0;
}