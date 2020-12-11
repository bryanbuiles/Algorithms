package otros

// https://www.hackerrank.com/challenges/taum-and-bday/problem
// Calcular el numero de regalos negros o blancos que hay que comprarW

// TaumBday ...
func TaumBday(b int32, w int32, bc int32, wc int32, z int32) int64 {
	var black, white, bcost, wcost, zi int64 = int64(b), int64(w), int64(bc), int64(wc), int64(z)
	if bcost > wcost {
		if bcost > wcost+zi {
			return ((black+white)*wcost + black*zi)
		}
	}
	if wcost > bcost+zi {
		return ((black+white)*bcost + white*zi)
	}
	return (black*bcost + white*wcost)
}
