// Jumping on the Clouds: Revisited
// https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

package otros

// JumpingOnClouds ...
func JumpingOnClouds(c []int32, k int32) int32 {
	var index, energy int32
	energy = 100
	len := int32(len(c))
	for index = 0; index < len; index += k {
		if index != 0 {
			energy--
			if c[index] != 0 {
				energy -= 2
			}
		}
		if index+k-len == 0 {
			if c[0] == 1 {
				energy -= 2
			} else {
				energy--
			}
			return energy
		}
		index = index - len

	}
	return energy
}
