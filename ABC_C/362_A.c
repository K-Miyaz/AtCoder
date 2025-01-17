#include<stdio.h>
#include<string.h>

void RGBprint(a, b){
    if(a < b){
        printf("%d", a);
    }
    else{
        printf("%d", b);
    }
}

int main(){
    int R, G, B;
    char C[100];

    scanf("%d %d %d", &R, &G, &B);
    scanf("%s", C);
    if(strcmp(C, "Red") == 0){
        RGBprint(G, B);
    }
    if(strcmp(C, "Blue") == 0){
        RGBprint(R, G);
    }
    if(strcmp(C, "Green") == 0){
        RGBprint(R, B);
    }
    return 0;
}