/*
Circular Array Rotation
https://www.hackerrank.com/challenges/circular-array-rotation/problem
*/

package arrays

// CircularArrayRotation ...
func CircularArrayRotation(a []int32, k int32, queries []int32) []int32 {

	len := int32(len(a))
	if len == 1 {
		return a
	}
	if len-k < 0 {
		k = k % len // el residuo me dice cuanto le falta para dar la vuelta completa
	}
	a = append(a[len-k:], a[:len-k]...) // append de dos listas
	for index := range queries {
		queries[index] = a[queries[index]]
	}
	return queries
}
