#include <stdio.h>
#include <string.h>

int main()
{
    char s[101], a[1];
    int len, ans = 0;

    scanf("%s", &s);
    len = strlen(s);
    a[0] = s[0];
    for (int i = 1; i < len; i++){
        if (s[i] != a[0] && ans == 0){
            ans = i + 1;
            continue;
        }
        if (s[i] != a[0] && ans != 0){
            ans = 0;
            break;
        }
    }
    if (ans == 0){
        ans = 1;
    }
    printf("%d", ans);
    return 0;
}