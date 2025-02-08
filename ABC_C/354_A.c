#include<stdio.h>
#include<math.h>

int main(){
    int i, H, tall;

    scanf("%d", &H);
    tall = 0;
    for(i = 0; tall <= H; i++){
        tall += pow(2, i);
    }
    printf("%d", i);

    return 0;
}