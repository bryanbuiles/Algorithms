package gredyalgoritm

/*
Luck Balance
https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
Hallar el maximo de suerte que tendra
*/

func luckBalance(k int32, contests [][]int32) int32 {
	var (
		arrLose             []int32
		index, nK, sumTotal int32
		saveIndex           int
	)
	lenCOntest := int32(len(contests))
	for index = 0; index < lenCOntest; index++ {
		if contests[index][1] == 1 {
			nK++
			if nK <= k && k > 0 {
				arrLose = append(arrLose, contests[index][0])
				sumTotal += contests[index][0]
			} else if k == 0 {
				sumTotal -= contests[index][0]
			} else {
				temp := arrLose[0]
				for indexSum, value := range arrLose {
					if temp >= value {
						saveIndex = indexSum
						temp = value
					}
				}
				if contests[index][0] > arrLose[saveIndex] {
					arrLose[saveIndex] = contests[index][0]
					sumTotal += contests[index][0] - (temp * 2)
				} else {
					sumTotal -= contests[index][0]
				}
			}
		} else {
			sumTotal += contests[index][0]
		}
	}
	return sumTotal
}

func isBalanced(s string) string {
	lenS := len(s)
	midLen := (lenS / 2) - 1
	contador := 1
	var n byte
	if lenS%2 != 0 {
		return "NO"
	}
	for index := range s {
		if s[index] == '(' {
			n = 1
		} else {
			n = 2
		}

		if s[index] != s[lenS-contador]-n {
			return "NO"
		}
		if index == midLen {
			break
		}
		contador++
	}
	return "YES"
}
