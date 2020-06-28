#include <stdio.h>
#include <stdlib.h>

#define POWER 33


int main(){
    int sizeint = sizeof(int);
    int word_number = POWER / sizeint + 1;

    int * bigdigit = malloc(word_number * sizeint);
    int shift = POWER - (sizeint * (word_number - 1));
    bigdigit[0] = 1 << shift;
    printf("%d ",bigdigit[0]);
    for(int i=1; i<word_number;i++){
        bigdigit[i] = 0;
        printf("%d ",bigdigit[i]);
    }
    printf("\n");
    int result = 0;
    for(int j=word_number-1;j>=0;){
        int tmp = 0;
        for(int i = word_number-1; i >= 0; i--){
            tmp = bigdigit[i] % 10;
            bigdigit[i] /= 10;
        }   
        result += tmp;
        if(bigdigit[j] != 0){
            continue;
        }else{
            j--;
        }
    }
    free(bigdigit);
    printf("result = %d\n",result);
    return 0;
}
