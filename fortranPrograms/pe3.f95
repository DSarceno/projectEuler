FUNCTION prime (n)
IMPLICIT NONE
REAL, INTENT(IN) :: n

LOGICAL :: prime
INTEGER :: i, sum

i = 2
sum = 0
DO
  IF (i == INT(CEILING(SQRT(n)))) EXIT
  IF (MOD(NINT(n),i) == 0) THEN
    sum = sum + i
  END IF

  i = i + 1
END DO

IF (sum /= 0) THEN
  prime = .FALSE.
ELSE
  prime = .TRUE.
END IF
END FUNCTION prime



PROGRAM pe3
IMPLICIT NONE
! @Author: Diego Sarceño
! Date: 11.1.2021
!
! Problem 3 Project Euler
!
! Purpose: Find the largest prime factor of 600851475143


! Declare function type
LOGICAL :: prime

REAL(8) :: p
INTEGER(8) :: i, np
p = 600851475143.
np = 0
i = 2

DO i = 2, NINT(p/2)
  IF ((MOD(INT(p,8),i) == 0) .AND. (prime(REAL(i,4)) .eqv. .TRUE.) .AND. (i >= np)) THEN
    np = i
  END IF
END DO

WRITE (*,*) np

END PROGRAM pe3
