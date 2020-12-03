package otros

/*
Este problema parte un numero en sus digitos 1023 en 1 0 2 3
Find Digits
https://www.hackerrank.com/challenges/find-digits/problem
*/

// FindDigits ...
func FindDigits(n int32) int32 {
	var residueNumber, number, contador int32
	number = n
	for number != 0 {
		residueNumber = number % 10
		if residueNumber != 0 {
			if n%residueNumber == 0 {
				contador++
			}
		}
		number /= 10
	}
	return contador
}
