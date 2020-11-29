package main

func jumpingOnClouds(c []int32) int32 {
	var contador, jump int32
	for _, number := range c {
		if number%2 == 0 {
			contador++
		} else {
			jump++
			if contador%2 != 0 {
				jump += contador / 2
			} else {
				jump += contador / 2
			}
			contador = 0
		}
	}
	if contador%2 != 0 {
		jump += contador / 2
	} else {
		jump += contador / 2
	}
	return jump
}
