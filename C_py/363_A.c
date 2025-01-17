#include<stdio.h>

int main(){
    int R;

    scanf("%d", &R);
    printf("%d", 100 - (R % 100));
}