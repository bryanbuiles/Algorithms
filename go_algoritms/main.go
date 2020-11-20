package main

import "fmt"

func main() {
	numeros := []int32{
		10, 20, 20, 10, 10, 30, 50, 10, 20,
	}
	var n int32 = 7
	fmt.Println(sockMerchant(n, numeros))
}
