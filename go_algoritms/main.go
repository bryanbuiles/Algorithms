package main

import (
	"fmt"
	"go_algoritms/arrays"
)

func main() {
	var num int32
	num = 4
	lista := []int32{1, 2, 3, 4, 5}
	fmt.Println(arrays.RotLeft(lista, num))
}
