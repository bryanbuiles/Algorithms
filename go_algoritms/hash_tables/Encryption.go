package hashtables

//https://www.hackerrank.com/challenges/encryption/problem
// encryption
// encripar una string siguiendo unas reglas

import (
	"math"
)

// Encryption ...
func Encryption(s string) string {
	hash := make(map[float64]string)
	len := float64(len(s))
	sqrt := math.Sqrt(len)
	mayor := math.Round(sqrt + 0.5)
	menor := math.Round(sqrt - 0.5)
	if math.Mod(len, menor) == 0 && menor*menor >= len {
		mayor = menor
	}
	var contador, flag, index float64
	for _, letters := range s {
		if flag != 0 {
			hash[contador] = hash[contador] + string(letters)
		} else {
			hash[contador] = string(letters)
		}
		contador++
		if contador > mayor-1 {
			contador = 0
			flag = 1
		}
	}
	var str1 string
	for index = 0; index < mayor; index++ {
		str1 += hash[index]
		if index < mayor-1 {
			str1 += " "
		}
	}
	return str1
}
