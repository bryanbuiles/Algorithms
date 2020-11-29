// Ejercicio hacker rank Arrays: Left Rotation
// correr los numeros a la izquierda "d" veces

package arrays

// RotLeft ...
func RotLeft(a []int32, d int32) []int32 {
	var d2 int
	a2 := make([]int32, len(a))
	d2 = int(d)
	len := len(a)
	for index, number := range a {
		position := index - d2
		if position < 0 {
			position = len + position
		}
		a2[position] = number
	}
	return a2
}
