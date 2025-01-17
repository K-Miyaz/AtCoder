#include<stdio.h>

int main(){
    int Y, Leap = 0;

    scanf("%d", &Y);
    if(Y % 4 == 0){
        Leap = 1;
        if(Y % 100 == 0){
            Leap = 0;
            if(Y % 400 == 0){
                Leap = 1;
            }
        }
    }
    if(Leap == 1){
        printf("366\n");
    }
    else{
        printf("365\n");
    }
    return 0;
}