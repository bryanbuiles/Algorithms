package main

import (
	"fmt"
	hashtables "go_algoritms/hash_tables"
)

func main() {
	str := "feedthedog"
	str = "haveaniceday"
	//str = "iffactsdontfittotheorychangethefacts"
	fmt.Println(hashtables.Encryption(str))
}
