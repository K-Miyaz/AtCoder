#include<stdio.h>

int main(){
  int N, T, A;
  int n;
  
  scanf("%d %d %d", &N, &T, &A);
  n = N / 2;
  
  if (T > n || A > n){
    printf("Yes");
  }
  else{
    printf("No");
  }
  return 0;
}