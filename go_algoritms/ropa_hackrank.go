/*
	Buscar cuantos pares de numeros de prendas del mismo color existen
*/

package main

func sockMerchant(n int32, ar []int32) int32 {
	dic := make(map[int32]int)
	var result int

	for _, ropa := range ar {
		_, ok := dic[ropa]
		if ok {
			dic[ropa]++
		} else {
			dic[ropa] = 1
		}
	}
	for _, dicNumber := range dic {
		result1 := dicNumber / 2
		result += result1
	}
	resultTotal := int32(result)
	return resultTotal
}
