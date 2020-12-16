package hashtables

/*
	Two Strings
	https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
	Mirar si dos arrays tienen almenos una similitud
*/

// TwoStrings ...
func TwoStrings(s1 string, s2 string) string {
	Dic := make(map[rune]string)
	for _, values := range s1 {
		Dic[values] = "YES"
	}
	for _, valuesS2 := range s2 {
		if _, ok := Dic[valuesS2]; ok {
			return "YES"
		}
	}
	return "NO"
}
