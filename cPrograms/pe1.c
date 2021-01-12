// @Author: Diego Sarceño
// Date: 11.1.2021
//
// Problem 1 Project Euler
//
// Purpose: Sum of all the multiples of 3 or 5 below 1000
#include <stdio.h>

int main( void ) {
  int sum, i;
  for (i = 1; i <= 1000; i++){
    if ((i % 3) && (i % 5)){
      sum += i;
    }
  }
  printf("%d \n", sum);
}
