/*
Sherlock and the Valid String
https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
Letras con la misma frecuencia con la posibilidad de eliminar una en el index
*/

package stringmanipulation

// IsValid ...
func IsValid(s string) string {
	wordMap := make(map[string]int)
	countMap := make(map[int]int)
	for _, words := range s {
		str := string(words)
		if _, ok := wordMap[str]; ok {
			wordMap[str]++
		} else {
			wordMap[str] = 1
		}
	}
	for _, values := range wordMap {
		if _, ok := countMap[values]; ok {
			countMap[values]++
		} else {
			countMap[values] = 1
		}
	}
	if len(countMap) == 1 {
		return "YES"
	}
	var contador, result, flag int
	if len(countMap) == 2 {
		for key, value := range countMap {
			if key == 1 && value == 1 {
				return "YES"
			}
			if contador == 1 {
				key *= -1
			}
			result += key
			if value == 1 {
				flag = 1
			}
			if flag == 1 && (result == 1 || result == -1) {
				return "YES"
			}
			contador++
		}
	}
	return "NO"
}
