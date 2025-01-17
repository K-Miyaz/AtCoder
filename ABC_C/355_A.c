#include<stdio.h>

int main(){
    int A, B;

    scanf("%d %d",&A, &B);

    if(A == B){
        printf("-1\n");
    }
    else{
        for(int i = 1; i <= 3; i++){
            if(i != A && i != B){
                printf("%d\n", i);
            }
        }
    }
    return 0;
}