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
	s := "[{"
	fmt.Println(isBalanced(s))

}

func isBalanced(s string) string {
	hasMap := map[rune]int{'(': 0, '[': 0, '{': 0}

	for index, values := range s {
		if values == '[' || values == '(' || values == '{' {
			hasMap[values]++
		} else {
			if index > 0 {
				if values == ')' && (s[index-1] == '[' || s[index-1] == '{') {
					return "NO"
				} else if values == ']' && (s[index-1] == '(' || s[index-1] == '{') {
					return "NO"
				} else if values == '}' && (s[index-1] == '(' || s[index-1] == '[') {
					return "NO"
				}
			}
			if values == ')' {
				hasMap[values-1]--
			} else {
				hasMap[values-2]--
			}
		}
		if hasMap['('] < 0 || hasMap['['] < 0 || hasMap['{'] < 0 {
			return "NO"
		}
	}
	if hasMap['('] == 0 && hasMap['['] == 0 && hasMap['{'] == 0 {
		return "YES"
	}
	return "NO"
}

// fmt.Printf("%c, %c\n", s[index], s[lenS-contador])
