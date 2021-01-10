/*
# https://www.hackerrank.com/challenges/queens-attack-2/problem
# Queen's Attack II no eficient
Hallar el numero de posiciones que puede estar la reina
*/

package main

import (
	"fmt"
)

func main() {
	var k int32
	array := []int32{1, 3, 5, 7, 9, 2}
	k = 3
	//array = []int32{1, 1, 1, 2, 2}
	fmt.Println(getMinimumCost(k, array))

}

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
