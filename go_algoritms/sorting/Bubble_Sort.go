package sorting

/*
Sorting: Bubble Sort
https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
Sorting array with bubble sort
*/

import "fmt"

// CountSwaps bubble sort
func CountSwaps(a []int32) {
	var numberOut, numberIn, temp, contador int32
	len := int32(len(a))
	for numberOut = 0; numberOut < len; numberOut++ {

		for numberIn = 0; numberIn < len-1; numberIn++ {
			// Swap adjacent elements if they are in decreasing order
			if a[numberIn] > a[numberIn+1] {
				temp = a[numberIn]
				a[numberIn] = a[numberIn+1]
				a[numberIn+1] = temp
				contador++
			}
		}

	}
	fmt.Println("Array is sorted in", contador, "swaps.")
	fmt.Println("First Element:", a[0])
	fmt.Println("Last Element:", a[len-1])
}
