#include<stdio.h>
#include<string.h>

int main(){
    char S[100], T[100];

    scanf("%s %s",S ,T);
    if((strcmp(S, "AtCoder") == 0) && (strcmp(T, "Land") == 0)){
        printf("Yes\n");
    }
    else{
        printf("No\n");
    }
    return 0;
}