#include <stdio.h>
#include <stdlib.h>

int *array_multiplication(const int power) {
    int *result = (int *) calloc((power / 2), sizeof(int));
    result[0] = 2;
    int digit = 0, carry = 0, x = 1;
    int *begin = NULL, *end = NULL;
    for(int i = 1; i < power; ++i) {
        begin = result;
        end = begin + x;
        while(begin != end) {
            digit = 2 * *begin + carry;
            carry = digit / 10;
            digit %= 10;
            *begin = digit;
            ++begin;
        }
        if(carry) {
            *begin = carry;
            carry = 0;
            ++x;
        }
    }
    return result;
}

int digit_sum(const int power) {
    int *temp = array_multiplication(power);
    int result = 0;
    for(int i = 0; i < power / 2; ++i) {
        result += temp[i];
    }
    free(temp);
    return result;
}

int main(int argc, const char * argv[]) {

    const int pow_1 = 15;
    const int pow_2 = 1000;
    const int pow_3 = 10000;
    printf("Sum of the digits of the number 2^%d: %d\n", pow_1, digit_sum(pow_1));
    printf("Sum of the digits of the number 2^%d: %d\n", pow_2, digit_sum(pow_2));
    printf("Sum of the digits of the number 2^%d: %d\n", pow_3, digit_sum(pow_3));

    return 0;
}
