#include<stdio.h>
#include<string.h>

int main(){
    int N, Len[100], Len_max = 0, Len_max_line[100];
    int i, j;
    char S[100][100], T[100][100];

    scanf("%d", &N);
    for(int i = 0; i < N; i++){
        scanf("%s",S[i]);
        Len[i] = strlen(S[i]);
        if(Len_max < Len[i]){
            Len_max = Len[i];
        }
    }
    for(i = 0; i < N; i++){
        for(j = 0; j < Len_max; j++){
            if(j < Len[i]){
                T[j][N - i - 1] = S[i][j];
            }
            else{
                T[j][N - i - 1] = '*';
            }
        }
    }
    for(i = 0; i < Len_max; i++){
        for(j = 0; j < N; j++){
            if(T[i][j] == '*'){
                continue;
            }
            else{
                Len_max_line[i] = j;
            }
        }
    }
    for(i = 0; i < Len_max; i++){
        for(j = 0; j <= Len_max_line[i]; j++){
            printf("%c",T[i][j]);
        }
        printf("\n");
    }
    return 0;
}