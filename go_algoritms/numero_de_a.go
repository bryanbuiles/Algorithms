/*
calcular el numero de letras "a"  hasta el indice n que se repiten en una string s = "abcac"
que se repite infinitamente  ejemplo "abcacabcacabcacabcac"

retornar el numero de veces que se repite la letra a hasta el indice n
*/
package main

func repeatedString(s string, n int64) int64 {
	var numberWords, index, numberA, maxA, indexF int64
	for _, letters := range s {
		if letters == 'a' {
			numberA++ // numero de letras a en la string s
		}
		index++ // len de la string
	}
	numberWords = n / index      // numero de string s que se repetiran en n
	maxA = numberWords * numberA // este es el numero maximo de letras a hasta n
	if n%index != 0 {            // si tiene residuo se suman las "a" restantes
		indexF = n - (numberWords * index)
		var index1 int64
		for index1 = 0; index1 < indexF; index1++ {
			if s[index1] == 'a' {
				maxA++
			}
		}
	}
	return maxA
}
