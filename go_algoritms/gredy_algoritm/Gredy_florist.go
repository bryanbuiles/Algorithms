/*
Greedy Florist
https://www.hackerrank.com/challenges/greedy-florist/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
Menor precio para comprar un numero n de flores
*/

package gredyalgoritm

func mergeSort(arr []int32) {

	lenArr := int32(len(arr))
	var (
		left  []int32
		right []int32
	)
	if lenArr > 1 {
		mid := lenArr / 2

		left = append(left, arr[:mid]...)
		right = append(right, arr[mid:]...)
		mergeSort(left)
		mergeSort(right)

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

func getMinimumCost(k int32, c []int32) int32 {
	var nCost, index, contadorTotal, contador int32
	mergeSort(c)
	lenC := int32(len(c))
	for index = lenC - 1; index >= 0; index-- {
		contadorTotal += ((nCost + 1) * c[index])
		contador++
		if contador%k == 0 {
			nCost++
		}
	}
	return contadorTotal
}
