/*
# https://www.hackerrank.com/challenges/queens-attack-2/problem
# Queen's Attack II no eficient
Hallar el numero de posiciones que puede estar la reina
*/

package arrays

func queensAttack(n int32, k int32, r_q int32, c_q int32, obstacles [][]int32) int32 {
	ostaclesMap := make(map[[2]int32]string)
	var arrObstacle [2]int32
	channel := make(chan int32)
	for _, values := range obstacles {
		arrObstacle[0] = values[0]
		arrObstacle[1] = values[1]
		ostaclesMap[arrObstacle] = "ok"
	}
	go func() {
		var contadorInt, i int32
		arr := [...]int32{r_q, c_q}
		cqgo := c_q - 1
		tempc := cqgo
		for i = 0; i < n; i++ {
			if tempc >= n-1 {
				break
			}
			tempc++
			arr[1] = tempc + 1
			_, ok := ostaclesMap[arr]
			if ok {
				break
			}
			contadorInt++
		}
		channel <- contadorInt
	}()
	go func() {
		var contadorInt, i int32
		arr := [...]int32{r_q, c_q}
		cqgo := c_q - 1
		tempc := cqgo
		for i = 0; i < n; i++ {
			if tempc <= 0 {
				break
			}
			tempc--
			arr[1] = tempc + 1
			_, ok := ostaclesMap[arr]
			if ok {
				break
			}
			contadorInt++
		}
		channel <- contadorInt
	}()
	// vertical right up
	go func() {
		var contadorInt, i int32
		arr := [...]int32{r_q, c_q}
		rqgo := r_q - 1
		cqgo := c_q - 1
		tempr := rqgo
		tempc := cqgo
		for i = 0; i < n; i++ {
			if tempc >= n-1 || tempr >= n-1 {
				break
			}
			tempr++
			tempc++
			arr[0] = tempr + 1
			arr[1] = tempc + 1
			_, ok := ostaclesMap[arr]
			if ok {
				break
			}
			contadorInt++
		}
		channel <- contadorInt
	}()
	// vertical down and left
	go func() {
		var contadorInt, i int32
		arr := [...]int32{r_q, c_q}
		rqgo := r_q - 1
		cqgo := c_q - 1
		tempr := rqgo
		tempc := cqgo
		for i = 0; i < n; i++ {
			if tempc <= 0 || tempr <= 0 {
				break
			}
			tempr--
			tempc--
			arr[0] = tempr + 1
			arr[1] = tempc + 1
			_, ok := ostaclesMap[arr]
			if ok {
				break
			}
			contadorInt++
		}
		channel <- contadorInt
	}()
	// vertical up left
	go func() {
		var contadorInt, i int32
		arr := [...]int32{r_q, c_q}
		rqgo := r_q - 1
		cqgo := c_q - 1
		tempr := rqgo
		tempc := cqgo
		for i = 0; i < n; i++ {
			if tempc <= 0 || tempr >= n-1 {
				break
			}
			tempr++
			tempc--
			arr[0] = tempr + 1
			arr[1] = tempc + 1
			_, ok := ostaclesMap[arr]
			if ok {
				break
			}
			contadorInt++
		}
		channel <- contadorInt
	}()
	// vertical down and right
	go func() {
		var contadorInt, i int32
		arr := [...]int32{r_q, c_q}
		rqgo := r_q - 1
		cqgo := c_q - 1
		tempr := rqgo
		tempc := cqgo
		for i = 0; i < n; i++ {
			if tempc >= n-1 || tempr <= 0 {
				break
			}
			tempr--
			tempc++
			arr[0] = tempr + 1
			arr[1] = tempc + 1
			_, ok := ostaclesMap[arr]
			if ok {
				break
			}
			contadorInt++
		}
		channel <- contadorInt
	}()
	// vertical up
	go func() {
		var contadorInt, i int32
		arr := [...]int32{r_q, c_q}
		rqgo := r_q - 1
		cqgo := c_q - 1
		tempr := rqgo
		tempc := cqgo
		for i = 0; i < n; i++ {
			if tempr >= n-1 {
				break
			}
			tempr++
			arr[0] = tempr + 1
			arr[1] = tempc + 1
			_, ok := ostaclesMap[arr]
			if ok {
				break
			}
			contadorInt++
		}
		channel <- contadorInt
	}()
	// vertical down
	go func() {
		var contadorInt, i int32
		arr := [...]int32{r_q, c_q}
		rqgo := r_q - 1
		tempr := rqgo
		for i = 0; i < n; i++ {
			if tempr <= 0 {
				break
			}
			tempr--
			arr[0] = tempr + 1
			_, ok := ostaclesMap[arr]
			if ok {
				break
			}
			contadorInt++
		}
		channel <- contadorInt
	}()
	var contadortotal int32
	for i := 0; i < 8; i++ {
		select {
		case contador := <-channel:
			contadortotal += contador
		}
	}
	return contadortotal
}
