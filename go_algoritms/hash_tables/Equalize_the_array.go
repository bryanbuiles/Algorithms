// Equalize the Array
// https://www.hackerrank.com/challenges/equality-in-a-array/problem

package hashtables

// EqualizeArray ...
func EqualizeArray(arr []int32) int32 {
	dic := make(map[int32]int32)
	len := int32(len(arr))
	var temp int32
	for _, number := range arr {
		dic[number]++
	}
	for _, values := range dic {
		if values > temp {
			temp = values
		}
	}
	return len - temp
}
