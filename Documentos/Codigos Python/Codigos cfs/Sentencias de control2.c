#include <stdio.h>
int main() {
   int numero, i=1;
   printf("Ingresa un numero para realizar su tabla de multiplicar: ");
   scanf("%d", &numero);

     for(int i = 1; i <= 10; i++){
        printf("%d * %d = %d \n", numero, i , numero * i);
    }
    return 0;
}
