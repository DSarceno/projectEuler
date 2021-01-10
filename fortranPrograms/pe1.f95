PROGRAM pe1
IMPLICIT NONE
! @Author: Diego Sarceño
! Date: 9.1.2021
!
! Problem 1 Project Euler
!
! Purpose: Sum of all the multiples of 3 or 5 below 1000
INTEGER :: i, n, sum

! Variable's declaration
n = 1000
i = 3
sum = 0
DO
  ! Loop limit
  IF (i == n) EXIT

  ! Add just 3 or 5 multiples
  IF ((MOD(i,3) == 0) .OR. (MOD(i,5) == 0)) THEN
    sum = sum + i
  END IF

  ! Counter
  i = i + 1
END DO

WRITE (*,*) sum

STOP
END PROGRAM pe1
