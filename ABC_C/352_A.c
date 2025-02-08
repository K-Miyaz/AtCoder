#include<stdio.h>

int main(){
    int N, X, Y, Z;

    scanf("%d %d %d %d", &N, &X, &Y, &Z);
    if(X < Y){
        if(X < Z && Z < Y){
            printf("Yes\n");
        }
        else{
            printf("No\n");
        }
    }
    else{
        if(Y < Z && Z < X){
            printf("Yes\n");
        }
        else{
            printf("No\n");
        }
    }
    return 0;
}