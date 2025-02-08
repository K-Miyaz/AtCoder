#include<stdio.h>
#include<stdlib.h>

//比較関数（昇順）
int cmp(const void* x, const void* y)
{
	if (*(int*)x > * (int*)y)
	{
		return 1;
	}
	else if (*(int*)x < *(int*)y)
	{
		return -1;
	}
	else
	{
		return 0;
	}
}

int main(){
    int N, i, second_A;
    scanf("%d", &N);
    int A[N], B[N];
    for(i = 0; i < N; ++i){
        scanf("%d ", &A[i]);
        B[i] = A[i];
    }
    qsort(A, N, sizeof(int), cmp);
    second_A = A[N - 2];
    for(i = 0; i < N; ++i){
        if(second_A == B[i]){
            printf("%d", i + 1);
        }
    }
    return 0;
}