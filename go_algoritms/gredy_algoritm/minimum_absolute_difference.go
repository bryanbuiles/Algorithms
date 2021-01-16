package gredyalgoritm

/*
Minimum Absolute Difference in an Array
https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
Calcular la minima diferencia absoluta de dos elementos en una array
*/

func minimumAbsoluteDifference(arr []int32) int32 {
	countInversions(arr)
	var suma, sumaTotal int32
	sumaTotal = arr[0] - arr[1]
	if sumaTotal < 0 {
		sumaTotal *= -1
	}
	for index, values := range arr {
		if sumaTotal == 0 {
			return 0
		}
		if index > 1 {
			suma = arr[index-1] - values
			if suma < 0 {
				suma *= -1
			}
			if suma < sumaTotal {
				sumaTotal = suma
			}
		}
	}
	return sumaTotal
}

func countInversions(arr []int32) {

	lenArr := int32(len(arr))
	var (
		left  []int32
		right []int32
	)
	if lenArr > 1 {
		mid := lenArr / 2

		left = append(left, arr[:mid]...)
		right = append(right, arr[mid:]...)
		countInversions(left)
		countInversions(right)

		var i, j, k int32
		lenL := int32(len(left))
		lenR := int32(len(right))
		for i < lenL && j < lenR {
			if left[i] < right[j] {
				arr[k] = left[i]
				i++
			} else {
				arr[k] = right[j]
				j++
			}
			k++
		}
		for i < lenL {
			arr[k] = left[i]
			i++
			k++
		}

		for j < lenR {
			arr[k] = right[j]
			j++
			k++
		}
	}
}
