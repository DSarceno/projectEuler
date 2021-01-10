PROGRAM pe2
IMPLICIT NONE
! @Author: Diego Sarceño
! Date: 9.1.2021
!
! Problem 2 Project Euler
!
! Purpose: Sum of all the even fibonacci numbers below 4000000
INTEGER :: a, b, step, sum

! Variable's declaration
a = 0
b = 1
sum = 0
DO
  ! Loop limit
  IF (a >= 4000000) EXIT

  ! Sum just the even Fib numbers
  IF (MOD(a,2) == 0) THEN
    sum = sum + a
  END IF

  ! Fibonacci step
  step = a + b
  a = b
  b = step
END DO

WRITE (*,*) sum

END PROGRAM pe2
