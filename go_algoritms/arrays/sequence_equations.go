/*
Sequence Equation
https://www.hackerrank.com/challenges/permutation-equation/problem
*/

package arrays

// PermutationEquation ...
func PermutationEquation(p []int32) []int32 {
	len := int32(len(p))
	dic := make(map[int32]int32)
	var index int32
	for index = 0; index < len; index++ {
		dic[p[index]] = index + 1

	}
	for index = 0; index < len; index++ {
		p[index] = dic[dic[index+1]]
	}
	return p
}
