/*
Sherlock and Anagrams
https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
Ejercicio importante, se usan varias cosas de go
Muestra como crear substrings de una misma array
*/

package hashtables

import (
	"sort"
	"strings"
)

// SherlockAndAnagrams ...
func SherlockAndAnagrams(s string) int32 {
	var i, j int
	var listLetter []string
	hashTable := make(map[string]int32)
	for _, letter := range s {
		listLetter = append(listLetter, (string(letter)))
	}
	for i = 0; i < len(s); i++ {
		for j = 0; j < len(s)-i; j++ { // fijarce como disminuye el espacio
			tmp := make([]string, i+1)
			copy(tmp, listLetter[j:j+i+1]) // fijarce como hace la substring
			sort.Strings(tmp)
			Strings := strings.Join(tmp, "")
			_, ok := hashTable[Strings]
			if ok {
				hashTable[Strings]++
			} else {
				hashTable[Strings] = 1
			}

		}
	}
	var totalAnag int32
	for _, values := range hashTable {
		totalAnag += (values - 1) * values / 2
	}
	return totalAnag
}
