/*
Balanced Brackets
https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues
Mirarsi los brackets estan balancados de acuerdo a su scope y frecuencia
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
*/

package stacksqueues

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
