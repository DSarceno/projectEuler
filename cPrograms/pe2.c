// @Author: Diego Sarceño
// Date: 11.1.2021
//
// Problem 1 Project Euler
//
// Purpose: Sum of all the even fibonacci numbers below 4000000

#include <stdio.h>

int main( void ){
  int a, b, step, sum; // Variable declaration

  // Values
  a = 0;
  b = 1;
  sum = 0;

  while (a <= 4000000){
    if (a % 2 == 0){
      sum += a;
    }
    step = a;
    a = b;
    b += step;
  }
  printf("%d \n", sum);
}
