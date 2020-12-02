// https://www.hackerrank.com/challenges/save-the-prisoner/problem
// save the prisoner
// un ejercicio muy bueno para aquellos ejercicios que pretenden recorren
// varias veces un ciclo

package otros

// SaveThePrisoner ...
func SaveThePrisoner(n int32, m int32, s int32) int32 {
	var total int32
	total = (m + s - 1) % n
	if total != 0 {
		return total
	}
	return n
}
