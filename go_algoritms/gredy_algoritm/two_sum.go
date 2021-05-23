package gredyalgoritm

/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
*/

func TwoSum(nums []int, target int) []int {
	var array [2]int
	mapNumbers := make(map[int]int)
	for index, number := range nums {
		theNumber := target - number
		if _, exist := mapNumbers[theNumber]; exist {
			array[0] = mapNumbers[theNumber]
			array[1] = index
			break
		}
		mapNumbers[number] = index
	}
	return array[:]
}
