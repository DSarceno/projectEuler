PROGRAM pe1
IMPLICIT NONE
! @Author: Diego Sarceño
! Date: 9.1.2021
!
! Problem 1 Project Euler
!
! Purpose: Sum of all the multiples of 3 or 5 below 1000
INTEGER :: i, n, sum

n = 1000
i = 3
sum = 0
DO
  IF (i == n) EXIT

  IF ((MOD(i,3) == 0) .OR. (MOD(i,5) == 0)) THEN
    sum = sum + i
  END IF
  i = i + 1
END DO

WRITE (*,*) sum

STOP
END PROGRAM pe1
