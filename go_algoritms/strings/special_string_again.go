/*
	Special String Again
	link: https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
	Fin de number of special substring if
	1) All of the characters are the same, e.g. aaa
	2) All characters except the middle one are the same, e.g. aadaa.
*/

package stringmanipulation

type letter struct {
	string
	int64
}

// SubstrCount ...
func SubstrCount(n int32, s string) int64 {

	var letters letter
	var listLetters []letter
	letters.string = string(s[0])
	letters.int64 = 0
	var i int32
	for i = 0; i < n; i++ {
		if string(s[i]) == letters.string {
			letters.int64++
		} else {
			listLetters = append(listLetters, letters)
			letters.string = string(s[i])
			letters.int64 = 1
		}
		if i == n-1 {
			listLetters = append(listLetters, letters)
		}
	}
	channel := make(chan int64)
	go sameletter(listLetters, channel)
	go oneLetter(listLetters, channel)
	a := <-channel
	b := <-channel

	return a + b
}

func sameletter(listLetters []letter, channel chan int64) {
	var contador int64
	for _, values := range listLetters {
		contador += ((values.int64 * (values.int64 + 1)) / 2)
	}
	channel <- contador
}

func oneLetter(listLetters []letter, channel chan int64) {
	var contador int64
	var j int32
	for j = 1; j < int32(len(listLetters)-1); j++ {
		if listLetters[j-1].string == listLetters[j+1].string && listLetters[j].int64 == 1 {
			if listLetters[j-1].int64 < listLetters[j+1].int64 {
				contador += listLetters[j-1].int64
			} else {
				contador += listLetters[j+1].int64
			}
		}
	}
	channel <- contador
}
