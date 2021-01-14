// @Author: Diego Sarceño
// Date: 11.1.2021
//
// Problem 3 Project Euler
//
// Purpose: Find the largest prime factor of 600851475143
// Compilation process: gcc -o pe3.out pe3.c -lm

#include <stdio.h>
#include <math.h>

int prime(double x);

int main( void ){
  double p;
  int j, np;
  double ceil(double x);
  double fmod(double x, double y);

  p = 600851475143;
  np = 0;

  for (j = 2; j = ceil(p/2); j++){
    if ((fmod(p,j) == 0) && (prime(j) == 1) && (j >= np)){
      np = j;
    }// end if
  }//end for

  printf("%d\n", np);

  return 0;
}

int prime(double x){
  int bool;
  int factors;
  double ceil(double x);
  double sqrt(double x);
  double fmod(double x, double y);
  for (unsigned int i = 2; i = ceil(sqrt(x)); i++){
    if (fmod(x,i) == 0){
      factors += i;
    }// end if
  }// end for

  if (factors == 0){
    bool = 1;
  }else{
    bool = 0;
  }
  return bool;
}// end function
