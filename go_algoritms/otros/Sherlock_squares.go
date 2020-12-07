package otros

//https://www.hackerrank.com/challenges/sherlock-and-squares/problem
// ejercicio de hallar las raices enteras en un rango de numeros en 0(1)

import (
	"math"
)

// Squares ...
func Squares(a int32, b int32) int32 {
	aFloat := float64(a)
	bFloat := float64(b)
	sqrta := math.Sqrt(aFloat)
	sqrtb := math.Sqrt(bFloat)
	resulta := math.Round(sqrta + 0.5)
	resultb := math.Round(sqrtb - 0.5)
	if math.Mod(aFloat, sqrta) == 0 {
		resulta = sqrta
	}
	result := (resultb + 1) - resulta
	return int32(result)
}
