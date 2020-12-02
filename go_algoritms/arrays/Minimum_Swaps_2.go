// minimum swaps 2 hacker rank
// calcular el minimo de swaps para tener una array ordenanada de numeros concecutivos
// y no repetidos

package arrays

// MinimumSwaps ...
func MinimumSwaps(arr []int32) int32 {
	var index, contador int32
	len := int32(len(arr))

	for index = 0; index < len; index++ {
		if (index + 1) != arr[index] {
			temp := arr[arr[index]-1]
			arr[arr[index]-1] = arr[index]
			arr[index] = temp
			contador++
		}
		if (index + 1) != arr[index] {
			index--
		}
	}
	return contador
}
