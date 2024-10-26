#include <stdio.h>

int main() {
   int numero, i=1;
   printf("Ingresa un numero para realizar su tabla de multiplicar: ");
   scanf("%d", &numero);
    while (i<=10){
        printf("%d*%d= %d\n", numero, i, numero * i);
        i++;
    }
    return 0;
}

