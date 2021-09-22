# include <stdio.h>
int main(void){
    char str1[] = "hello word";
    char str2[] = "hello word";
    char* str3 = "hello word";
    char* str4 = "hello word";
    if(str1 == str2)
        printf("1==2");
    else
        printf("1!=2");
    if(str3 == str4)
        printf("3==4");
    else
        printf("3!=4");
    return 0;
}
